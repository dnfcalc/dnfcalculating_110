<script lang="tsx">
  import { IJadeInfo } from "@/api/info/type"
  import { useBasicInfoStore, useConfigStore } from "@/store"
  import { getFloat } from "@/utils"
  import { computed, defineComponent, renderList } from "vue"

  export default defineComponent({
    name: "jade",
    setup(props, { emit, slots }) {
      const basicInfoStore = useBasicInfoStore()
      const configStore = useConfigStore()

      const currentInfo = function <T>(name: string, defaultValue?: T) {
        return computed<string | number>({
          get() {
            return configStore.getForge("jade", name) ?? defaultValue ?? 0
          },
          set(val) {
            configStore.setForge("jade", name, val)
          }
        })
      }

      const valueList = computed(() => {
        return function (id: number = -1) {
          if (id == -1) return undefined
          else {
            let res = []
            const cur = basicInfoStore.jade_info?.find(e => e.id == id) as IJadeInfo
            if (cur) {
              const { max, min, unit, pre } = cur
              //
              if (pre == 0) {
                res.push({
                  id: 1,
                  value: unit
                })
              } else {
                for (let i = Number(max) as number; i >= Number(min); ) {
                  if (i != 0) {
                    res.push({
                      id: getFloat(i, 1),
                      value: (i > 0 ? "+" : "") + getFloat(i, 1) + unit
                    })
                  }
                  i = Number((i - Number(pre)).toFixed(1))
                }
              }
              return res
            }
          }
        }
      })

      // 辟邪玉
      const jade_First = currentInfo("jade_First")

      const jade_Second = currentInfo("jade_Second")

      const jade_Third = currentInfo("jade_Third")

      const jade_Fourth = currentInfo("jade_Fourth")

      return () => (
        <div>
          <div class="flex mt-5px">
            <calc-select v-model={jade_First.value} class="!h-20px flex-1 !mr-10px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.jade_info ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>

            <calc-select class="!h-20px flex-1">
              {renderList(valueList.value(Number(jade_First.value)) ?? [], item => (
                <calc-option value={item.id}>{item.value}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="flex mt-5px">
            <calc-select v-model={jade_Second.value} class="!h-20px flex-1 !mr-10px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.jade_info ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>

            <calc-select class="!h-20px flex-1">
              {renderList(valueList.value(Number(jade_Second.value)) ?? [], item => (
                <calc-option value={item.id}>{item.value}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="flex mt-5px">
            <calc-select v-model={jade_Third.value} class="!h-20px flex-1 !mr-10px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.jade_info ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>

            <calc-select class="!h-20px flex-1">
              {renderList(valueList.value(Number(jade_Third.value)) ?? [], item => (
                <calc-option value={item.id}>{item.value}</calc-option>
              ))}
            </calc-select>
          </div>

          <div class="flex mt-5px">
            <calc-select v-model={jade_Fourth.value} class="!h-20px flex-1 !mr-10px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.jade_info ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>

            <calc-select class="!h-20px flex-1">
              {renderList(valueList.value(Number(jade_Fourth.value)) ?? [], item => (
                <calc-option value={item.id}>{item.value}</calc-option>
              ))}
            </calc-select>
          </div>
        </div>
      )
    }
  })
</script>
