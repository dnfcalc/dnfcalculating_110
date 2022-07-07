<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import { TreeNode } from "@/components/calc/tree/types"
  import Profile from "@/components/internal/profile.vue"
  import { useBasicInfoStore, useCharacterStore, useConfigStore, useDetailsStore } from "@/store"
  import featureList from "@/utils/featureList"

  import EquipIcon from "@/components/internal/equip/eq-icon.vue"

  import EquipInfo from "@/components/internal/equip/eq-info.vue"
  import { useOpenWindow } from "@/hooks/open"
  import { syncRef, useAsyncState, useDebounceFn } from "@vueuse/core"
  import { computed, defineComponent, onUnmounted, reactive, ref, renderList, watch } from "vue"
  import RecommendsVue from "./recommends.vue"
  import { rarityClass } from "@/utils"

  export interface IJadeUpgrade {
    id: number
    name: string
    damage: number
    percent: string
    color: string
  }

  type FilterFunction = (e: IEquipmentInfo) => boolean

  export default defineComponent({
    async setup() {
      const configStore = useConfigStore()
      const basicStore = useBasicInfoStore()
      const detailsStore = useDetailsStore()
      const charcaterStore = useCharacterStore()

      const characterStore = useCharacterStore()

      const armor_types = ["布甲", "皮甲", "轻甲", "重甲", "板甲"]
      const armor_parts = ["上衣", "头肩", "下装", "鞋", "腰带"]

      const jewel_parts = ["项链", "戒指", "手镯"]

      const special_parts = ["辅助装备", "魔法石", "耳环"]

      const else_parts = ["称号", "宠物"]

      const filter = ref<FilterFunction | null>(null)

      const items = computed<TreeNode[]>(() => {
        return [
          {
            label: "全部类别",
            value: "-1",
            onSelect() {
              filter.value = null
            }
          },
          {
            label: "武器",
            value: "武器",
            onSelect() {
              filter.value = e => e.part == "武器"
              choose_part.value = "武器"
            },
            children: characterStore.weapon_types.map(r => {
              return {
                label: r,
                value: r,
                onSelect() {
                  filter.value = e => e.type == r && e.part == "武器"
                  choose_part.value = "武器"
                }
              }
            })
          },
          {
            label: "防具",
            value: "防具",
            onSelect() {
              filter.value = e => armor_parts.includes(e.part)
            },
            children: armor_parts.map(part => {
              return {
                label: part,
                value: part,
                onSelect() {
                  filter.value = e => e.part == part
                  choose_part.value = part
                },
                children: armor_types.map(t => {
                  return {
                    label: t,
                    value: `${part}_${t}`,
                    onSelect() {
                      filter.value = e => e.type == t && e.part == part
                      choose_part.value = part
                    }
                  }
                })
              }
            })
          },
          {
            label: "首饰",
            value: "首饰",
            onSelect() {
              filter.value = e => jewel_parts.includes(e.part)
            },
            children: jewel_parts.map(part => {
              return {
                label: part,
                value: part,
                onSelect() {
                  filter.value = e => e.part == part
                  choose_part.value = part
                }
              }
            })
          },
          {
            label: "特殊装备",
            value: "特殊装备",
            onSelect() {
              filter.value = e => special_parts.includes(e.part)
            },
            children: special_parts.map(part => {
              return {
                label: part,
                value: part,
                onSelect() {
                  filter.value = e => e.part == part
                  choose_part.value = part
                }
              }
            })
          },
          {
            label: "其它",
            value: "其它",
            onSelect() {
              filter.value = e => special_parts.includes(e.part)
            },
            children: else_parts.map(part => {
              return {
                label: part,
                value: part,
                onSelect() {
                  filter.value = e => e.part == part
                  choose_part.value = part
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
        if (!!rarity.value) {
          list = list.filter(r => r.rarity == rarity.value)
        }

        return list
      })

      const show_list = computed(() => {
        const start = (pagination.page - 1) * pagination.pageSize
        const end = start + pagination.pageSize
        return equips.value.slice(start, end)
      })

      const choose_item = ref("武器")
      const choose_part = ref("武器")

      function reset() {
        choose_feature.value = []
        keyword.cache = ""
        keyword.value = ""
        choose_item.value = "武器"
        choose_part.value = "武器"
        pagination.page = 1
      }

      syncRef(choose_item, choose_part, { direction: "rtl" })

      const selectEquip = ref<ID>()

      const keyword = reactive({
        value: "",
        cache: ""
      })

      const rarity = ref("")

      function chooseEqu(equ: IEquipmentInfo, toggle = false) {
        return (event: Event) => {
          event.preventDefault()
          selectEquip.value = equ.id
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
        page: 1,
        pageSize: 14
      })

      const total = computed(() => equips.value.length)
      const total_page = computed(() => Math.ceil(total.value / pagination.pageSize))

      watch(total_page, () => {
        pagination.page = 1
      })

      syncRef(
        computed(() => show_list.value[0]?.id),
        selectEquip,
        { direction: "ltr" }
      )

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
          <span class="cursor-pointer h-4 mt-1 mr-2 leading-4 inline-block calc-tag" onClick={removeFeature}>
            #{feat.label}
          </span>
        )
      }

      function search() {
        keyword.value = keyword.cache
        pagination.page = 0
      }

      const result = useAsyncState(
        () => configStore.calc(true),
        { id: undefined, equips: [], role: "delear", name: "", alter: "", skills: {}, total_data: [0], info: undefined, skills_passive: undefined, jade: undefined, equips_forget: {} },
        { resetOnExecute: false }
      )

      const stopWatch = watch(
        () => charcaterStore.calc_token,
        () => {
          result.execute()
        }
      )

      onUnmounted(() => {
        stopWatch()
      })

      const curEquList = computed(() => {
        return basicStore.equipment_list.filter(item => configStore.single_set.includes(item.id)).sort((a, b) => Number(a.id) - Number(b.id))
      })

      watch(
        curEquList,
        useDebounceFn(async val => {
          if (val.length < 1) {
            return
          }
          await result.execute()
        }, 200)
      )

      const openUrl = useOpenWindow()

      const openDetail = () => openUrl(`/result`, { query: { res: `${result.state.value.id}`, standard: `${detailsStore.standard_uuid}` }, width: 890, height: 600 })

      function setStandard() {
        if (result.state.value.total_data[0] > 0) {
          detailsStore.setStandard(result.state.value.id)
        }
      }

      const jade = computed(() => {
        let temp: IJadeUpgrade[] = []
        const damage = result.state.value.total_data[0]
        result.state.value.jade
          ?.sort((a, b) => b.damage - a.damage)
          .forEach((item, index) => {
            let x = (index / (result.state.value.jade?.length ?? 1)) * 10 - 3
            let y = 1 / (1 + Math.exp(-x))
            temp.push({
              id: item.id,
              name: item.name,
              damage: item.damage,
              percent: damage == 0 ? "- -" : ((item.damage.round(0) / damage.round(0)) * 100 - 100).toFixed(2) + "%",
              color: `rgb(${Math.trunc(255 - 80 * y)},${Math.trunc(245 - 100 * y)},${Math.trunc(0 + 150 * y)})`
            })
          })
        return temp.sort((a, b) => a.id - b.id)
      })

      const recommendVisible = ref(false)

      async function showRecommend() {
        recommendVisible.value = true
      }

      const singleRef = ref<HTMLElement | null>(null)

      return () => (
        <div class="flex singleset" ref={singleRef}>
          <calc-dialog lazy header="流派推荐(玩家上传)" v-model:visible={recommendVisible.value}>
            <RecommendsVue v-model:visible={recommendVisible.value}></RecommendsVue>
          </calc-dialog>

          <div class="flex flex-col m-7px mb-0">
            <div class="w-125">
              <div class=" w-full">
                <div class="w-full pb-1.5">
                  <div class="bg-hex-000000/45 py-2 px-2 justify-between items-center">
                    <div class="flex space-x-2 mb-2 items-center ">
                      <calc-cascader v-model={choose_item.value} items={items.value} placeholder="请输入名称搜索" class="flex-1 !h-5"></calc-cascader>
                      <calc-select class="!h-5" v-show={characterStore.is_delear} v-model={rarity.value} placeholder="品质">
                        <calc-option value={""}>全部</calc-option>
                        <calc-option value="智慧产物">智慧产物</calc-option>
                        <calc-option value="史诗">史诗</calc-option>
                        <calc-option value="神话">神话</calc-option>
                        <calc-option value="传说">传说</calc-option>
                        <calc-option value="稀有">稀有</calc-option>
                      </calc-select>
                      <calc-autocomplete onEnter={search} placeholder="请输入名称搜索" class="flex-1 !h-5" v-model={keyword.cache}></calc-autocomplete>
                      <calc-button onClick={search} title="搜索" class="ml-2" icon="search"></calc-button>
                      <calc-button onClick={reset} title="重置" class="ml-4" icon="reset"></calc-button>
                    </div>

                    <div class="flex">
                      <calc-select
                        input-class="calc-tags-input"
                        label={labelTag}
                        multiple
                        multiple-limit={5}
                        class="flex-1 !h-5"
                        v-model={choose_feature.value}
                        emptyLabel="请选择#标签,最多可选择4个#标签"
                      >
                        {renderList(featureList, item => (
                          <calc-option value={item.value}></calc-option>
                        ))}
                      </calc-select>
                      <calc-button small class="ml-2" onClick={clearFeature}>
                        清空
                      </calc-button>
                      <calc-button onClick={showRecommend} small class="ml-2">
                        流派推荐
                      </calc-button>
                    </div>
                  </div>
                </div>
                <div class="flex h-142  w-full">
                  <div class="h-full bg-hex-0d0d0d mx-2px w-48%">
                    <calc-selection v-model={selectEquip.value} active-class="equip-line-selected" class="h-[calc(100%-2.5rem)]">
                      {renderList(show_list.value, item => {
                        return (
                          <calc-item title="右键点击穿戴" onContextmenu={chooseEqu(item)} value={item.id} class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border">
                            <div class="h-full w-full top-0 left-0 absolute mask"></div>
                            <EquipIcon onClick={chooseEqu(item, true)} eq={item}></EquipIcon>
                            <span class={["text-xs", "ml-4", rarityClass(item.rarity ?? "")]}>{item.name}</span>
                            <span class={["h-4 w-6"].concat(isChoose(item) ? "icon-checked" : "")}></span>
                          </calc-item>
                        )
                      })}
                      {renderList(pagination.pageSize - show_list.value.length, i => (
                        <div class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border"></div>
                      ))}
                    </calc-selection>
                    <calc-pagination disabled={recommendVisible.value} v-model:page={pagination.page} total-page={total_page.value} v-show={total_page.value > 0}></calc-pagination>
                  </div>

                  <div class="h-full bg-hex-0d0d0d w-52% s-left">
                    <div class="h-115 w-full pb-4 overflow-y-auto !max-w-100%">
                      <EquipInfo eid={selectEquip.value} />
                    </div>
                    <div class=" bg-hex-0e0e0e h-17 p-2 items-start">
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
            </div>
          </div>
          <div>
            <div class="flex h-24px mt-7px items-center justify-between !mr-8px !ml-8px">
              <calc-button class="!w-30%" onClick={setStandard}>
                设为基准
              </calc-button>
              <calc-button class="!w-30%" onClick={() => detailsStore.setStandard(undefined)}>
                清空基准
              </calc-button>
              <calc-button class="!w-30%" onClick={() => openDetail()}>
                查看详情
              </calc-button>
            </div>
            <Profile
              standard-data={detailsStore.standard?.total_data}
              details={result.state.value.info}
              total-data={result.state.value.total_data}
              role={charcaterStore.role}
              equ-list={curEquList.value}
              class="m-5px !mt-0 !mr-2px !ml-2px"
              equips_forget={result.state.value.equips_forget}
              v-model:part={choose_part.value}
              canChoose={true}
            ></Profile>
          </div>
          {result.state.value.jade && (
            <div class="flex flex-col mt-0 mr-2px mb-0 ml-2px w-350px items-center">
              <div class="flex h-30px w-100% justify-center items-center">辟邪玉提升率(理论值仅供参考)</div>
              {renderList(jade.value ?? [], item => (
                <div class="flex h-30px w-100%" style={"color:" + item.color}>
                  <div class="flex w-70% items-center justify-center">{item.name}</div>
                  <div class="flex w-30% items-center justify-center">{item.percent}</div>
                </div>
              ))}
            </div>
          )}
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .calc-tags-input {
    .calc-tag {
      text-decoration: underline;
      text-underline-offset: 2px;
      color: #ffb400 !important;

      &:hover {
        color: #fff000 !important;
      }
    }
  }
</style>

<style lang="scss" scoped>
  .equip-line {
    border: 1px solid transparent;
    background-image: url("@/assets/img/dictionary_line.png");
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

  .icon-checked {
    background-image: url("@/assets/img/item_checked.png");
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
  }

  .singleset {
    .equ {
      display: flex;
      flex-wrap: wrap;
      padding: 5px;
      background-color: rgba(0, 0, 0, 0.45);
      .equ-item {
        width: 30px;
        height: 30px;
        background-color: rgba(0, 0, 0, 0.5);
        border: 1px solid #1a1a1a;
        margin-right: 4px;
        margin-bottom: 4px;

        // &:hover {
        //   width: 30px;
        //   height: 30px;
        //   z-index: 3;
        //   background-image: url(@/assets/img/item_hover.png);
        //   background-size: 100% 100%;
        // }
      }
    }

    .s-left {
      .approved-form {
        width: calc(100% - 23px);
      }
    }
  }
</style>
