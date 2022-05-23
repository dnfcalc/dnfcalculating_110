<script lang="tsx">
  import { defineComponent, ref, renderList, computed, reactive, watch, onMounted } from "vue"
  import { useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store"
  import featureList from "@/utils/featureList"
  import { TriggerSet } from "@/api/info/type"

  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import EquipList from "@/components/internal/equip/equip-list.vue"

  export default defineComponent({
    components: { EquipTips, EquipList },
    async setup() {
      const basicStore = useBasicInfoStore()
      const choose_feature = ref(0)

      const highlight = computed<number[]>({
        get() {
          return equips.value.map(e => (e.features?.includes(choose_feature.value) ? e.id : 0)).filter(e => e > 0)
        },
        set(val) {
          if (val.length === 0) {
            choose_feature.value = 0
          }
        }
      })

      const characterStore = useCharacterStore()
      const configStore = useConfigStore()

      const equips = computed(() => basicStore.equipment_info?.lv110 ?? [])

      const weapons = computed(() => basicStore.equipment_info?.weapon ?? [])

      const myths = computed(() => basicStore.equipment_info?.myth ?? [])

      const wisdom = computed(() => basicStore.equipment_info?.wisdom ?? [])

      const selected_110 = computed({
        get() {
          return configStore.lv110_list
        },
        set(val: number[]) {
          configStore.lv110_list = val
        }
      })

      const selected_weapons = computed({
        get() {
          return configStore.weapons_list
        },
        set(val: number[]) {
          configStore.weapons_list = val
        }
      })

      const selected_myths = computed({
        get() {
          return configStore.myths_list
        },
        set(val: number[]) {
          configStore.myths_list = val
        }
      })

      const selected_wisdom = computed({
        get() {
          return configStore.wisdom_list
        },
        set(val: number[]) {
          configStore.wisdom_list = val
        }
      })

      watch(configStore.wisdom_list, () => {
        configStore.customizeInit()
      })

      watch(configStore.myths_list, () => {
        configStore.customizeInit()
      })

      watch(configStore.weapons_list, () => {
        configStore.customizeInit()
      })

      watch(configStore.lv110_list, () => {
        configStore.customizeInit()
      })

      const trigger_list = computed(() => basicStore.trigger_list ?? [])

      // 没有的就补，多的就删

      // watch(triggers, val => {
      //   characterStore.trigger_set = val
      //   console.log(characterStore.trigger_set)
      // })

      // let equi_choose = computed<EquiChooseState[]>(() => {
      //   let list = [] as EquiChooseState[]
      //   basic_info.value?.public_110_equ?.forEach(item => {
      //     if (item.state) {
      //       list.push({ id: item.id, state: false })
      //     }
      //   })
      //   return list
      // })

      return () => (
        <div class="flex">
          <EquipList v-model:selected={selected_110.value} class="equ-105" v-model:highlight={highlight.value} showHighlight={choose_feature.value > 0} list={equips.value} title="Lv110装备">
            {{
              header() {
                return (
                  <calc-select v-model:modelValue={choose_feature.value} class="ownSelect" emptyLabel="特性选择">
                    <calc-option value={0}>全部特性</calc-option>
                    {renderList(featureList, item => (
                      <calc-option value={item.value}>{item.label}</calc-option>
                    ))}
                  </calc-select>
                )
              }
            }}
          </EquipList>
          <div class="equ-else">
            <EquipList v-model:selected={selected_myths.value} class="equ-else-sort" list={myths.value} title="神话装备" />
            <EquipList v-model:selected={selected_wisdom.value} class="equ-else-sort" list={wisdom.value} title="智慧产物" />
            <EquipList v-model:selected={selected_weapons.value} class="equ-else-sort" list={weapons.value} title="武器列表" />
            {
              //<EquipList class="equ-else-sort" list={weapons.value} title="称号" />
            }
          </div>
          <div class="equ-trigger">
            {trigger_list.value &&
              renderList(trigger_list.value, (trigger, index) => (
                <>
                  {configStore.trigger_set[index] && (
                    <calc-select multiple v-model={configStore.trigger_set[index].select} class="ownSelect-2">
                      {renderList(trigger.selectList, (item, index) => (
                        <>
                          <calc-option value={index}>{item}</calc-option>
                        </>
                      ))}
                    </calc-select>
                  )}
                </>
              ))}
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .equ-105 {
    margin: 5px;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    width: 420px;
    background-color: rgba(255, 255, 255, 0.1);
    .item {
      width: 30px;
      height: 34px;
      margin-left: 6px;

      &:nth-child(11n + 6),
      &:nth-child(11n + 9) {
        margin-left: 15px;
      }
    }
  }

  .ownSelect {
    height: calc(100% - 2px) !important;
    width: 200px !important;
    margin-right: 3px;
  }

  .ownSelect-2 {
    height: 24px !important;
    width: calc(50% - 10px) !important;
    margin: 2px;
  }

  .equ-else {
    display: flex;
    flex-direction: column;
    width: 260px;
    margin-bottom: 5px;
    .equ-else-sort {
      margin-top: 5px;

      display: flex;
      flex-wrap: wrap;
      align-content: flex-start;
      background-color: rgba(255, 255, 255, 0.1);
      .item {
        width: 30px;
        height: 34px;
        margin-left: 6px;
        // &:nth-child(7n + 1) {
        //   margin-left: 0px;
        // }
      }
    }
  }

  .equ-trigger {
    width: 400px;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    margin-top: 3px;
  }

  .imgcover::after {
    content: "";
    width: 28px;
    height: 28px;
    background-color: rgba(50, 50, 50, 0.75);
    z-index: 999;
  }
</style>
