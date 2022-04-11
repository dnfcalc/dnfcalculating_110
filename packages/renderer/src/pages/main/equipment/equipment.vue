<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList } from "vue"
  import { useBasicInfoStore } from "@/store"
  import { IEquipmentInfo } from "@/api/info/type"

  export interface BasicInfo {
    public_110_equ?: IEquipmentInfo[]
    char_weapon_info?: any
  }

  export default defineComponent(() => {
    const basicStore = useBasicInfoStore()
    let basic_info = ref<BasicInfo>({})
    onMounted(async () => {
      await basicStore.get_equipment_info()
      basic_info.value.public_110_equ =
        basicStore?.equipmentinfo as IEquipmentInfo[]
    })

    function itemInfo(equ: IEquipmentInfo) {
      return () => {
        console.log(basicStore.get_equipment_detail(equ.id))
      }
    }

    return () => (
      <div>
        <div class="equ">
          <calc-button class="w-100% mt-5px mb-5px">105装备</calc-button>
          {renderList(
            basic_info.value.public_110_equ as IEquipmentInfo[],
            (equ, index) => (
              <div class="item" onMouseenter={itemInfo(equ)}>
                <img src={"./images/equipment/" + equ.icon} />
              </div>
            )
          )}
        </div>
      </div>
    )
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
</style>
