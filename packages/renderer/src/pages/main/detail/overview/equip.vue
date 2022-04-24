<script lang="tsx">
  import { useBasicInfoStore, useCharacterStore, useDetailsStore } from "@/store"
  import { computed, defineComponent, renderList, PropType, ref } from "vue"
  import { IEnchantingInfo } from "@/api/info/type"
  export default defineComponent({
    name: "equip",
    setup(props, { emit, slots }) {
      const detailsStore = useDetailsStore()
      const characterStore = useCharacterStore()
      const can_upgrade = computed(() => ["称号", "宠物"].indexOf(detailsStore.part as string) < 0)
      const has_socket = computed(() => ["称号", "宠物", "耳环", "武器"].indexOf(detailsStore.part as string) < 0)
      const has_socket_right = computed(() => !["辅助装备", "魔法石"].includes(detailsStore.part as string))
      const has_wisdom = computed(() => ["称号", "宠物", "武器"].indexOf(detailsStore.part as string) < 0)
      const basicInfoStore = useBasicInfoStore()

      const enchanting_list = computed<IEnchantingInfo[] | undefined>(() => {
        return basicInfoStore.enchanting_info?.filter(item => item.position.includes(detailsStore.part)).sort((a, b) => (b.maxFrame ?? 0) - (a.maxFrame ?? 0))
      })

      const emblem_list = computed<IEnchantingInfo[] | undefined>(() => {
        return basicInfoStore.emblem_info?.filter(item => item.position.includes(detailsStore.part))
      })

      const global_change = ref(true)

      const currentInfo = function <T>(name: string, defaultValue?: T) {
        return computed<string | number>({
          get() {
            return characterStore.getForge(detailsStore.part, name) ?? defaultValue ?? 0
          },
          set(val) {
            if (global_change.value) {
              let parts: string[] = []
              let appendName = ""
              if (name === "enchanting") {
                const enchant = basicInfoStore.enchanting_info?.find(item => item.id == val) as IEnchantingInfo | undefined
                if (enchant?.position) {
                  parts = enchant.position.split("，")
                }
              }
              if (name === "socket_left" || name === "socket_right") {
                const enchant = basicInfoStore.emblem_info?.find(item => item.id.toString() == val.toString()) as IEnchantingInfo | undefined
                if (enchant?.position) {
                  parts = enchant.position.split("，").filter(item => !["皮肤", "武器装扮"].includes(item))
                }
                appendName = ["socket_left", "socket_right"].filter(item => item !== name)[0]
              }
              if (["cursed_type", "cursed_number", "growth_First", "growth_Second", "growth_Third", "growth_Fourth"].includes(name)) {
                parts = detailsStore.display_parts.filter(e => !["称号", "宠物"].includes(e))
              }
              if (parts.length) {
                parts.forEach(e => characterStore.setForge(e, name, val))
                if (appendName) parts.forEach(e => characterStore.setForge(e, appendName, val))
              }
            }
            characterStore.setForge(detailsStore.part, name, val)
          }
        })
      }

      //附魔
      const enchanting = currentInfo<string | number>("enchanting")

      // 镶嵌栏1
      const socket_left = currentInfo<string | number>("socket_left", "0")

      // 镶嵌栏2
      const socket_right = currentInfo<string | number>("socket_right")

      // 增幅
      const cursed_type = currentInfo<string | number>("cursed_type")

      const cursed_number = currentInfo<string | number>("cursed_number")

      const wisdom_number = currentInfo<string | number>("wisdom_number")

      const dz_number = currentInfo<string | number>("dz_number")

      const growth_First = currentInfo<string | number>("growth_First", 1)

      const growth_Second = currentInfo<string | number>("growth_Second", 1)

      const growth_Third = currentInfo<string | number>("growth_Third", 1)

      const growth_Fourth = currentInfo<string | number>("dz_Fourth", 1)

      return () => {
        return (
          <div class="flex flex-wrap equ-profile">
            <div class="equ-profile-item">
              <div class="row-name mr-10px">当前部位</div>
              {detailsStore.part}

              {can_upgrade.value ? <calc-checkbox style="margin-left:auto" v-model={global_change.value} label="全局修改"></calc-checkbox> : <div></div>}
            </div>
            {can_upgrade.value ? (
              <div class="equ-profile-item">
                <div class="row-name">增幅</div>
                <calc-select v-model={cursed_type.value} class="!h-20px flex-1">
                  <calc-option value={1}>增幅</calc-option>
                  <calc-option value={2}>强化</calc-option>
                </calc-select>
                <calc-select v-model={cursed_number.value} class="!h-20px flex-1">
                  {renderList(32, i => (
                    <calc-option value={i - 1}>{i - 1}</calc-option>
                  ))}
                </calc-select>
                {has_wisdom.value ? (
                  <calc-select v-model={wisdom_number.value} class="!h-20px flex-1">
                    {renderList(32, i => (
                      <calc-option value={i - 1}>改造+ {i - 1}</calc-option>
                    ))}
                  </calc-select>
                ) : (
                  <calc-select v-model={dz_number.value} class="!h-20px flex-1">
                    {renderList(9, i => (
                      <calc-option value={i - 1}>锻造+ {i - 1}</calc-option>
                    ))}
                  </calc-select>
                )}
              </div>
            ) : (
              <div></div>
            )}
            <div class="equ-profile-item">
              <div class="row-name">附魔</div>
              <calc-select v-model={enchanting.value} class="!h-20px flex-1">
                <calc-option value={0}>无</calc-option>
                {renderList(enchanting_list.value ?? [], item => (
                  <calc-option value={item.id}>{item.props}</calc-option>
                ))}
              </calc-select>
            </div>
            {has_socket.value ? (
              <div class="equ-profile-item">
                <div class="row-name">徽章</div>
                <calc-select v-model={socket_left.value} class="!h-20px flex-1">
                  <calc-option value={0}>无</calc-option>
                  {renderList(emblem_list.value ?? [], item => (
                    <calc-option value={item.id}>{`${item.rarity}${item.type}徽章[${item.props}]`}</calc-option>
                  ))}
                </calc-select>
                {has_socket_right.value && (
                  <calc-select v-model={socket_right.value} class="!h-20px flex-1">
                    <calc-option value={0}>无</calc-option>
                    {renderList(emblem_list.value ?? [], item => (
                      <calc-option value={item.id}>{`${item.rarity}${item.type}徽章[${item.props}]`}</calc-option>
                    ))}
                  </calc-select>
                )}
              </div>
            ) : (
              <div></div>
            )}
            {can_upgrade.value ? (
              <div class="equ-profile-item">
                <div class="row-name">成长属性</div>
                <calc-select v-model={growth_First.value} class="!h-20px flex-1">
                  {renderList(100, i => (
                    <calc-option value={i}>属性1 Lv{i}</calc-option>
                  ))}
                </calc-select>
                <calc-select v-model={growth_Second.value} class="!h-20px flex-1">
                  {renderList(100, i => (
                    <calc-option value={i}>属性2 Lv{i}</calc-option>
                  ))}
                </calc-select>
                <calc-select v-model={growth_Third.value} class="!h-20px flex-1">
                  {renderList(100, i => (
                    <calc-option value={i}>属性3 Lv{i}</calc-option>
                  ))}
                </calc-select>
                <calc-select v-model={growth_Fourth.value} class="!h-20px flex-1">
                  {renderList(100, i => (
                    <calc-option value={i}>属性4 Lv{i}</calc-option>
                  ))}
                </calc-select>
              </div>
            ) : (
              <div></div>
            )}
          </div>
        )
      }
    }
  })
</script>

<style lang="scss"></style>
