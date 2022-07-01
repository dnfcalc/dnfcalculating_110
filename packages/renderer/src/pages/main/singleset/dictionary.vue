<script lang="tsx">
  import { IEquipmentInfo } from "@/api/info/type"
  import { TreeNode } from "@/components/calc/tree/types"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import EquipInfo from "@/components/internal/equip/eq-info.vue"
  import featureList from "@/utils/featureList"

  import { useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store"
  import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"

  export default defineComponent({
    setup() {
      const characterStore = useCharacterStore()
      const basicStore = useBasicInfoStore()
      const items = computed<TreeNode[]>(() => [
        {
          label: "全部类别",
          value: -1
        },
        {
          label: "武器",
          children: characterStore.weapon_types.map(r => {
            return {
              label: r,
              value: r
            }
          })
        }
      ])

      const choose_feature = ref(0)

      const equips = computed(() =>
        (basicStore.equipment_info?.lv110 ?? []).filter(r => {
          return r.name.includes(keyword.value.trim()) && (choose_feature.value == 0 || r.features?.includes(choose_feature.value))
        })
      )

      const show_list = computed(() => {
        const start = pagination.page * pagination.pageSize
        const end = start + pagination.pageSize
        return equips.value.slice(start, end)
      })

      const selectEquip = ref<ID>()

      const keyword = ref("")

      const configStore = useConfigStore()

      function chooseEqu(equ: IEquipmentInfo) {
        return () => {
          if (!equ?.id) {
            return
          }
          const index = equips.value.findIndex(item => item.typeName == equ.typeName)
          if (index < 0) {
            configStore.single_set.push(equ.id)
          } else {
            configStore.single_set[index] = equ.id
          }
          configStore.single_set = configStore.single_set.filter(r => !!r)
        }
      }

      const pagination = reactive({
        page: 0,
        pageSize: 12
      })

      const total = computed(() => equips.value.length)
      const total_page = computed(() => Math.ceil(total.value / pagination.pageSize))

      watch(total_page, () => {
        pagination.page = 0
      })

      watch(
        () => pagination.page,
        () => {
          selectEquip.value = show_list.value[0]?.id
        }
      )

      function pop(step: number) {
        return () => {
          let page = pagination.page + step
          page = Math.max(page, 0)
          page = Math.min(page, total_page.value - 1)
          pagination.page = page
          console.log(page)
        }
      }

      return () => (
        <div class=" w-full">
          <div class="w-full py-2">
            <div class="flex bg-hex-000000/45 justify-between items-center">
              <calc-select class="!h-25px !w-40%" v-model={choose_feature.value} emptyLabel="特性选择">
                <calc-option value={0}>全部特性</calc-option>
                {renderList(featureList, item => (
                  <calc-option value={item.value}>{item.label}</calc-option>
                ))}
              </calc-select>
              名称搜索:
              <calc-autocomplete class="ml-10px !w-40%" v-model={keyword.value}></calc-autocomplete>
            </div>{" "}
          </div>
          <div class="flex h-128 w-full">
            <div class="h-full bg-hex-0d0d0d mx-2px w-50%">
              <calc-selection v-model={selectEquip.value} active-class="equip-line-selected">
                {renderList(show_list.value, item => {
                  return (
                    <calc-item onDblclick={chooseEqu(item)} value={item.id} class="flex h-9 px-2px items-center justify-between equip-line">
                      <EquipTips eq={item} key={item.id} canClick={true} show-tips={false}></EquipTips>
                      <span class="text-xs ml-4 text-hex-ffb400">{item.name}</span>
                      <calc-button onClick={chooseEqu(item)}>穿戴</calc-button>
                    </calc-item>
                  )
                })}
              </calc-selection>
              <div v-show={total_page.value > 1} class="flex space-x-4 h-8 w-full items-center justify-center">
                <calc-button disabled={pagination.page < 1} class="min-w-5" onClick={pop(-1)}>
                  &lt;
                </calc-button>
                <span class="text-center w-12">
                  {pagination.page + 1}/{total_page.value}
                </span>
                <calc-button disabled={pagination.page >= total_page.value - 1} class="min-w-5" onClick={pop(1)}>
                  &gt;
                </calc-button>
              </div>
            </div>

            <div class="h-full bg-hex-0d0d0d  w-50%  overflow-y-auto">
              <EquipInfo class="w-full" eid={selectEquip.value} />
            </div>
          </div>
        </div>
      )
    }
  })
</script>
<style lang="scss">
  .equip-line {
    border: 2px solid transparent;
    background-color: #0d0d0d;
    &:hover:not(.equip-line-selected) {
      border: 2px solid #055577;
    }

    &-selected {
      border: 2px solid #ffb400;
    }
  }
</style>
