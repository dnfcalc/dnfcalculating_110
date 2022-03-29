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
    return () => (
      <div>
        {renderList(
          basic_info.value.public_110_equ as IEquipmentInfo[],
          (equ, index) => (
            <img src={"./images/equipment/" + equ.icon} />
          )
        )}
      </div>
    )
  })
</script>
