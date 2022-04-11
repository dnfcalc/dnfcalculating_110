<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList } from "vue"
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
      let equi_choose = ref<EquiChooseState[]>([])

      onMounted(async () => {
        await basicStore.get_equipment_info()
        basic_info.value.public_110_equ =
          basicStore?.equipmentinfo as IEquipmentInfo[]

        basic_info.value.public_110_equ.forEach(item => {
          equi_choose.value.push({ id: item.id, state: false })
        })
      })

      return () => (
        <div>
          <div class="equ">
            <calc-button class="w-100% mb-5px">105装备</calc-button>
            {renderList(
              basic_info.value.public_110_equ as IEquipmentInfo[],
              (equ, index) => (
                <equip-tips
                  eq={equ}
                  canClick={true}
                  show-tips
                  v-model:useActive={equi_choose.value[index].state}
                ></equip-tips>
              )
            )}
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
    width: 370px;
    .item {
      width: 30px;
      height: 32px;
    }
    .item:nth-child(11n + 6),
    :nth-child(11n + 9) {
      margin-left: 10px;
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
