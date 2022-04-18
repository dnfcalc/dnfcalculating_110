<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, computed, reactive } from "vue"
  import { useBasicInfoStore } from "@/store"
  import { IEquipmentInfo, IWeaponInfo } from "@/api/info/type"
  import featureList from "@/utils/featureList"

  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import { useRoute } from "vue-router"
  import EquipList from "@/components/internal/equip-list.vue"
  import item from "@/components/base/item"

  export default defineComponent({
    components: { EquipTips, EquipList },
    setup() {
      const basicStore = useBasicInfoStore()
      const route = useRoute()
      const choose_feature = ref(0)

      const equips = computed(() => basicStore.equipment_info?.equipment_Lv110 ?? [])

      const highlight = computed(() => equips.value.map(e => (e.features?.includes(choose_feature.value) ? e.id : 0)).filter(e => e > 0))

      const weapons = computed(() => basicStore.equipment_info?.equipment_weapon.filter(item => item.name == route.params.name)[0].eqs ?? [])

      const myths = computed(() => basicStore.equipment_info?.equipment_myth ?? [])

      const wisdom = computed(() => basicStore.equipment_info?.equipment_wisdom ?? [])

      const selected = ref<number[]>([])

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
          <EquipList v-model:selected={selected.value} class="equ-105" highlight={highlight.value} showHighlight={choose_feature.value > 0} list={equips.value} title="Lv110装备">
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
            <EquipList list={myths.value} title="神话装备" />
            <EquipList list={wisdom.value} title="智慧产物" />
            <EquipList list={weapons.value} title="武器列表" />
            <EquipList list={weapons.value} title="称号 " />
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

  .imgcover::after {
    content: "";
    width: 28px;
    height: 28px;
    background-color: rgba(50, 50, 50, 0.75);
    z-index: 999;
  }
</style>
