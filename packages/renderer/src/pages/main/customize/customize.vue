<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"
  import { useBasicInfoStore, useConfigStore } from "@/store"
  export default defineComponent(() => {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()

    const equs = computed(() => {
      const list = [...configStore.wisdom_list, ...configStore.myths_list, ...configStore.weapons_list, ...configStore.lv110_list, ...configStore.single_set]
      return basicStore.equipment_list.filter(item => list.findIndex(e => Number(e) == Number(item.id)) >= 0 && item.alternative.length > 0) ?? []
    })

    return () => (
      <div>
        {renderList(equs.value, item => (
          <div>{item.name}</div>
        ))}
      </div>
    )
  })
</script>
