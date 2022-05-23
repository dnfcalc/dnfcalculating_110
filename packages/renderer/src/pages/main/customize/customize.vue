<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"
  import { useBasicInfoStore, useConfigStore } from "@/store"
  export default defineComponent(() => {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()

    const equs = computed(() => {
      const temp =
        basicStore.equipment_list.filter(
          item =>
            [...configStore.wisdom_list, ...configStore.myths_list, ...configStore.weapons_list, ...configStore.lv110_list, ...configStore.single_set].findIndex(e => Number(e) == Number(item.id)) >=
              0 && item.alternative.length > 0
        ) ?? []
      const list = temp.map(item => item.id)
      const keys = Object.keys(configStore.customize)
      ;(keys.filter(item => list.indexOf(Number(item)) < 0) ?? []).forEach(item => delete configStore.customize[item])
      list.filter(item => keys.indexOf(item.toString()) < 0).forEach(item => (configStore.customize[item] = [0, 0, 0, 0]))
      return basicStore.equipment_list.filter(item => list.findIndex(e => Number(e) == Number(item.id)) >= 0 && item.alternative.length > 0) ?? []
    })

    return () => (
      <div class="flex flex-wrap mt-5px">
        {renderList(equs.value, a => (
          <div class="cus-item">
            <img src={"./images/equipment/" + a.icon} />
            {renderList(4, index => (
              <calc-select class="w-100%">
                {renderList(a.alternative, b => (
                  <calc-option>{b}</calc-option>
                ))}
              </calc-select>
            ))}
          </div>
        ))}
      </div>
    )
  })
</script>

<scss lang="scss">
.cus-item {
  width: 180px;
  height: 120px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-around;
}
</scss>
