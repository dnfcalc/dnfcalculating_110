<script lang="tsx">
  import { IEnchantingInfo } from "@/api/info/type"
  import { useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store"
  import { syncRef } from "@vueuse/core"
  import { computed, defineComponent, renderList } from "vue"

  export default defineComponent({
    name: "clothes",
    setup() {
      const basicInfoStore = useBasicInfoStore()
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()

      const emblem_list = computed<IEnchantingInfo[] | undefined>(() => {
        return basicInfoStore.details?.emblem?.filter(item => item.rarity != "白金").sort((a, b) => (b.maxFame ?? 0) - (a.maxFame ?? 0))
      })

      const equipInfo = function <T>(part: string, name: string, defaultValue?: T) {
        return computed<T>({
          get() {
            return configStore.getForge(part, name) ?? defaultValue ?? 0
          },
          set(val) {
            if (val !== undefined) {
              configStore.setForge(part, name, val)
            }
          }
        })
      }

      const up_skill = computed(() => characterStore.clothes_coat)
      const down_skill = computed(() => characterStore.clothes_pants)
      // 武器装扮
      const wqzb_enchat = equipInfo<string | number>("武器装扮", "enchanting")
      const wqzb_left = equipInfo<string | number>("武器装扮", "socket_left")
      const wqzb_right = equipInfo<string | number>("武器装扮", "socket_right")

      // 皮肤
      const pf_enchat = equipInfo<string | number>("皮肤", "enchanting")
      const pf_left = equipInfo<string | number>("皮肤", "socket_left")
      const pf_right = equipInfo<string | number>("皮肤", "socket_right")
      // 光环
      const gh_enchat = equipInfo<string | number>("光环", "enchanting")
      const gh_left = equipInfo<string | number>("光环", "socket_left")
      const gh_right = equipInfo<string | number>("光环", "socket_right")

      syncRef(wqzb_left, wqzb_right, { direction: "ltr" })
      syncRef(pf_left, pf_right, { direction: "ltr" })
      syncRef(gh_left, gh_right, { direction: "ltr" })

      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">武器装扮</div>
            <calc-select v-model={wqzb_enchat.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.details?.enchanting.filter(item => item.position.includes("武器装扮")) ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={wqzb_left.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={wqzb_right.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">皮肤</div>
            <calc-select v-model={pf_enchat.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.details?.enchanting?.filter(item => item.position.includes("皮肤")) ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={pf_left.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={pf_right.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">光环</div>
            <calc-select v-model={gh_enchat.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(basicInfoStore.details?.enchanting.filter(item => item.position.includes("光环")) ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={gh_left.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={gh_right.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(emblem_list.value ?? [], item => (
                <calc-option value={item.id}>{`${item.type}[${item.props}]`}</calc-option>
              ))}
            </calc-select>
          </div>
          {renderList(basicInfoStore.details?.dress ?? {}, (list, part) => {
            const current = computed({
              get() {
                if (!configStore.dress_set[part]) {
                  configStore.dress_set[part] = {
                    id: list[0].id,
                    option: ""
                  }
                }

                return configStore.dress_set[part]
              },
              set(val) {
                configStore.dress_set[part] = {
                  id: val.id,
                  option: val.option
                }
              }
            })

            const options = computed(() => {
              return list.find(e => e.id == current.value.id)?.options ?? []
            })

            return (
              <div class="equ-profile-item">
                <div class="row-name">{part}</div>
                <calc-select v-model={current.value.id} class="flex-1 !h-20px">
                  {renderList(list, item => (
                    <calc-option value={item.id}>{item.name}</calc-option>
                  ))}
                </calc-select>
                <calc-select v-model={current.value.option} class="flex-1 !h-20px">
                  <calc-option value={0}>其他</calc-option>
                  {renderList(options.value, (item, i) => (
                    <calc-option value={item}>{item}</calc-option>
                  ))}
                </calc-select>
              </div>
            )
          })}
          {
            // 暂时无法解决渲染触发change事件 后面实现
            //   <div class="equ-profile-item">
            //     <div class="row-name">套装</div>
            //     <calc-select class="flex-1 !h-20px" onChange={chageSuit}>
            //       {renderList(clothes_type, (item, index) => (
            //         <calc-option value={index}>{item + "套装"}</calc-option>
            //       ))}
            //     </calc-select>
            //     <div class="flex-1"></div>
            //   </div>
          }
        </div>
      )
    }
  })
</script>
