<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import { TreeNode } from "@/components/calc/tree/types"
  import EquipIcon from "@/components/internal/equip/eq-icon.vue"

  import EquipInfo from "@/components/internal/equip/eq-info.vue"
  import featureList from "@/utils/featureList"

  import { useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store"
  import { syncRef } from "@vueuse/core"
  import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"

  type FilterFunction = (e: IEquipmentInfo) => boolean

  export default defineComponent({
    setup() {
      const characterStore = useCharacterStore()
      const basicStore = useBasicInfoStore()
      const armor_types = ["布甲", "皮甲", "轻甲", "重甲", "板甲"]
      const armor_parts = ["上衣", "头肩", "下装", "鞋", "腰带"]

      const jewel_parts = ["项链", "戒指", "手镯"]

      const special_parts = ["辅助装备", "魔法石", "耳环"]

      const filter = ref<FilterFunction | null>(null)

      const items = computed<TreeNode[]>(() => {
        return [
          {
            label: "全部类别",
            value: -1,
            onSelect() {
              filter.value = null
            }
          },
          {
            label: "武器",
            onSelect() {
              filter.value = e => e.part == "武器"
            },
            children: characterStore.weapon_types.map(r => {
              return {
                label: r,
                value: r,
                onSelect() {
                  filter.value = e => e.type == r && e.part == "武器"
                }
              }
            })
          },
          {
            label: "防具",
            onSelect() {
              filter.value = e => armor_parts.includes(e.part)
            },
            children: armor_parts.map(part => {
              return {
                label: part,
                onSelect() {
                  filter.value = e => e.part == part
                },
                children: armor_types.map(t => {
                  return {
                    label: t,
                    value: `${part}_${t}`,
                    onSelect() {
                      filter.value = e => e.type == t && e.part == part
                    }
                  }
                })
              }
            })
          },
          {
            label: "首饰",
            onSelect() {
              filter.value = e => jewel_parts.includes(e.part)
            },
            children: jewel_parts.map(part => {
              return {
                label: part,
                value: part,
                onSelect() {
                  filter.value = e => e.part == part
                }
              }
            })
          },
          {
            label: "特殊装备",
            onSelect() {
              filter.value = e => special_parts.includes(e.part)
            },
            children: special_parts.map(part => {
              return {
                label: part,
                value: part,
                onSelect() {
                  filter.value = e => e.part == part
                }
              }
            })
          }
        ]
      })

      const choose_feature = ref<ID[]>([])

      const equips = computed(() => {
        let list = basicStore.equipment_list ?? []
        list = list.filter(r => {
          const feats = choose_feature.value.filter(r => !!r)
          return r.name.includes(keyword.value.trim()) && (feats.length == 0 || feats.every(f => r.features?.includes(f)))
        })
        if (!!filter.value && filter.value instanceof Function) {
          list = list.filter(filter.value)
        }
        console.log(Array.from(new Set(list.map(r => r.rarity))))
        if (!!rarity.value) {
          console.log(
            rarity.value,
            list.map(r => r.rarity)
          )
          list = list.filter(r => r.rarity == rarity.value)
        }

        return list
      })

      const show_list = computed(() => {
        const start = pagination.page * pagination.pageSize
        const end = start + pagination.pageSize
        return equips.value.slice(start, end)
      })

      function reset() {
        choose_feature.value = []
        keyword_cache.value = ""
        keyword.value = ""
        pagination.page = 0
      }

      const selectEquip = ref<ID>()

      const keyword_cache = ref("")

      const keyword = ref("")

      const rarity = ref("史诗")

      const configStore = useConfigStore()

      function chooseEqu(equ: IEquipmentInfo, toggle = false) {
        return (event: Event) => {
          event.stopPropagation()
          event.preventDefault()
          configStore.addSingle(equ.id, toggle)
        }
      }

      const chooseEquFeature = computed(() => {
        {
          const id = selectEquip.value
          if (id) {
            const equ = show_list.value.find(e => e.id == id)
            if (equ) {
              const featIds = equ.features ?? []
              return featureList.filter(r => featIds.includes(r.value))
            }
          }
          return []
        }
      })

      function isChoose(equ: IEquipmentInfo) {
        return configStore.single_set.includes(equ.id)
      }

      const pagination = reactive({
        page: 0,
        pageSize: 10
      })

      const total = computed(() => equips.value.length)
      const total_page = computed(() => Math.ceil(total.value / pagination.pageSize))

      watch(total_page, () => {
        pagination.page = 0
      })

      syncRef(
        computed(() => show_list.value[0]?.id),
        selectEquip,
        { direction: "ltr" }
      )

      function gotoPage(page: number) {
        page = Math.max(page, 0)
        page = Math.min(page, total_page.value - 1)
        pagination.page = page
        console.log(page)
      }

      function chooseFeature(id: ID) {
        if (!choose_feature.value.includes(id) && choose_feature.value.length < 4) {
          choose_feature.value.push(id)
        }
      }

      function clearFeature() {
        choose_feature.value = []
      }

      function labelTag(value: number) {
        const feat = featureList.find(e => e.value == value)
        if (!feat) {
          return <span></span>
        }

        function removeFeature() {
          const index = choose_feature.value.indexOf(value)
          if (index > -1) {
            choose_feature.value.splice(index, 1)
          }
        }
        return (
          <span class="cursor-pointer h-4 mt-1 mr-2 leading-4 inline-block feat-tag" onClick={removeFeature}>
            #{feat.label}
          </span>
        )
      }

      function search() {
        keyword.value = keyword_cache.value
        pagination.page = 0
      }

      return () => (
        <div class=" w-full">
          <div class="w-full py-2">
            <div class="bg-hex-000000/45 py-2 px-2 justify-between items-center">
              <div class="flex space-x-2 mb-2 items-center ">
                <calc-cascader default-value={-1} items={items.value} placeholder="请输入名称搜索" class="flex-1 !h-5"></calc-cascader>
                <calc-select class="!h-5" v-show={characterStore.is_delear} v-model={rarity.value} placeholder="品质">
                  <calc-option value={""}>全部</calc-option>
                  <calc-option value="智慧产物">智慧产物</calc-option>
                  <calc-option value="史诗">史诗</calc-option>
                  <calc-option value="神话">神话</calc-option>
                </calc-select>
                <calc-autocomplete onEnter={search} placeholder="请输入名称搜索" class="flex-1 !h-5" v-model={keyword_cache.value}></calc-autocomplete>
                <calc-button onClick={search} title="搜索" class="ml-2" icon="search"></calc-button>
                <calc-button onClick={reset} title="重置" class="ml-4" icon="reset"></calc-button>
              </div>

              <div class="flex">
                <calc-select
                  input-class="text-hex-ffb400 hover:text-hex-fff000 feat-input "
                  label={labelTag}
                  multiple
                  multiple-limit={5}
                  class="flex-1 !h-5"
                  v-model={choose_feature.value}
                  emptyLabel="请选择#标签,最多可选择4个#标签"
                >
                  {renderList(featureList, item => (
                    <calc-option value={item.value}>{item.label}</calc-option>
                  ))}
                </calc-select>
                <calc-button class="ml-2 py-0 !h-5 !leading-5" onClick={clearFeature}>
                  清空
                </calc-button>
              </div>
            </div>
          </div>
          <div class="flex h-108  w-full">
            <div class="h-full bg-hex-0d0d0d mx-2px  w-50%">
              <calc-selection v-model={selectEquip.value} active-class="equip-line-selected" class="h-[calc(100%-3rem)]">
                {renderList(show_list.value, item => {
                  return (
                    <calc-item title="右键点击穿戴" onContextmenu={chooseEqu(item)} value={item.id} class="flex h-9 mb-2px px-1 items-center equip-line relative box-border">
                      <div class="h-full w-full top-0 left-0 absolute mask"></div>
                      <EquipIcon onClick={chooseEqu(item, true)} hightlight={isChoose(item)} eq={item}></EquipIcon>
                      <span class="text-xs ml-4 text-hex-ffb400">{item.name}</span>
                    </calc-item>
                  )
                })}
              </calc-selection>
              <calc-pagination page={pagination.page} onChange={gotoPage} total-page={total_page.value} v-show={total_page.value > 0}></calc-pagination>
            </div>

            <div class="h-full bg-hex-0d0d0d  w-50% ">
              <div class="h-92 w-full overflow-y-auto">
                <EquipInfo class="  w-full overflow-y-auto" eid={selectEquip.value} />
              </div>
              <div class=" bg-hex-0e0e0e h-16 p-2 items-start">
                {chooseEquFeature.value?.length ? (
                  renderList(chooseEquFeature.value, feat => (
                    <div onClick={() => chooseFeature(feat.value)} class="cursor-pointer h-4 mt-1 mr-2 text-hex-ffb400 leading-4 inline-block underline underline-offset-2 hover:text-hex-fff000">
                      #{feat.label}
                    </div>
                  ))
                ) : (
                  <div class="cursor-pointer h-4 mt-1 mr-2  text-hex-86784f leading-4 inline-block underline underline-offset-2 ">#无标签</div>
                )}
              </div>
            </div>
          </div>
        </div>
      )
    }
  })
</script>
<style lang="scss">
  .equip-line {
    border: 1px solid transparent;
    background-image: url("./img/dictionary_line.png");
    background-repeat: no-repeat;
    background-size: 100% 100%;
    &:hover {
      .mask {
        background-image: url("@/assets/img/hover_mask.png");
        background-repeat: no-repeat;
        background-size: 100% 100%;
      }
    }

    &-selected {
      border: 1px solid #ffb400;
    }
  }

  .feat-input {
    .feat-tag {
      text-decoration: underline;
      text-underline-offset: 2px;
    }
  }
</style>
