<script lang="tsx">
  import { useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store"
  import { computed, defineComponent, renderList } from "vue"
  export default defineComponent(() => {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()
    const characterStore = useCharacterStore()

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
      list.filter(item => keys.indexOf((item ?? "").toString()) < 0).forEach(item => (configStore.customize[item ?? ""] = [0, 0, 0, 0]))
      return basicStore.equipment_list.filter(item => list.findIndex(e => Number(e) == Number(item.id)) >= 0 && item.alternative.length > 0) ?? []
    })

    const entry_list = computed(() => basicStore.entry_list)

    const entry = (index: number) => {
      const info = entry_list.value?.[index]
      if (characterStore.is_buffer) return `[${info?.buff}] ${info?.props.join(",")}`
      return `[${info?.attack}] ${info?.props.join(",")}`
    }
    return () => (
      <div class="flex flex-wrap mt-5px">
        {equs.value.length > 0 &&
          renderList(equs.value, a => (
            <div class="cus-item">
              <img src={"/images/equipment/" + a.icon} />
              {renderList(4, index => (
                <div class="mt-5px">
                  <calc-select class="!h-20px !w-530px" v-model={configStore.customize[a.id ?? ""][index - 1]}>
                    <calc-option value={0}>无</calc-option>
                    {renderList(
                      a.alternative?.filter(item => configStore.customize[a.id ?? ""].filter((a, i) => index - 1 != i).indexOf(item) < 0),
                      b => (
                        <calc-option value={b}>{entry(b)}</calc-option>
                      )
                    )}
                  </calc-select>
                </div>
              ))}
            </div>
          ))}
      </div>
    )
  })
</script>

<scss lang="scss">
.cus-item {
  width: 540px;
  margin-top: 5px;
  margin-left: 3px;
  display: flex;
  align-items: center;
  flex-direction: column;
}
</scss>
