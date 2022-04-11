<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, computed } from "vue"
  import { useBasicInfoStore } from "@/store"
  import { IEquipmentInfo } from "@/api/info/type"

  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"

  interface BasicInfo {
    public_110_equ?: IEquipmentInfo[]
    char_weapon_info?: any
  }

  interface EquiChooseState {
    id: number
    state: boolean
  }

  export default defineComponent({
    components: { EquipTips },
    setup(props, { emit, slots }) {
      const basicStore = useBasicInfoStore()
      let basic_info = ref<BasicInfo>({})

      onMounted(async () => {
        await basicStore.get_equipment_info()
        basic_info.value.public_110_equ =
          basicStore?.equipmentinfo as IEquipmentInfo[]
        basic_info.value?.public_110_equ.forEach(item => {
          item.state = false
          // 这里检查存档，更新 state
        })
      })

      function changeState(equ: IEquipmentInfo) {
        return (e: boolean) => {
          equ.state = e
          console.log(equi_choose.value)
        }
      }

      let equi_choose = computed<EquiChooseState[]>(() => {
        let list = [] as EquiChooseState[]
        basic_info.value?.public_110_equ?.forEach(item => {
          if (item.state) {
            list.push({ id: item.id, state: false })
          }
        })
        return list
      })

      return () => (
        <div>
          <div class="equ">
            <calc-button class="w-100% mb-5px">105装备</calc-button>
            <div>
              {renderList(
                basic_info.value.public_110_equ as IEquipmentInfo[],
                (equ, index) => (
                  <equip-tips
                    class="item"
                    eq={equ}
                    canClick={true}
                    show-tips
                    active={equ.state}
                    onChange={changeState(equ)}
                  ></equip-tips>
                )
              )}
            </div>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .equ {
    margin: 5px;
    display: flex;
    flex-wrap: wrap;
    align-content: space-between;
    justify-content: space-between;
    align-items: center;
    width: 366px;
    .item {
      width: 30px;
      height: 32px;

      &:nth-child(11n + 6),
      &:nth-child(11n + 9) {
        margin-left: 7px;
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
