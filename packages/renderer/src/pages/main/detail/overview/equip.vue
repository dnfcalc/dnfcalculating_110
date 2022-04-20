<script lang="tsx">
  import { useBasicInfoStore, useCharacterStore, useDetailsStore } from "@/store"
  import { computed, defineComponent, renderList, PropType, ref } from "vue"
  import { IDetailInfo } from "../type"
  import { IEnchantingInfo } from "@/api/info/type"
  import itemIcon from "@/components/internal/item-icon"
  export default defineComponent({
    name: "equip",
    props: {
      currentDetail: {
        type: Object as PropType<IDetailInfo>,
        required: true
      }
    },
    setup(props, { emit, slots }) {
      const detailsStore = useDetailsStore()
      const characterStore = useCharacterStore()
      const can_upgrade = computed(() => ["称号", "宠物"].indexOf(detailsStore.part as string) < 0)
      const has_socket = computed(() => ["称号", "宠物", "耳环", "武器"].indexOf(detailsStore.part as string) < 0)
      const has_wisdom = computed(() => ["称号", "宠物", "武器"].indexOf(detailsStore.part as string) < 0)
      const basicInfoStore = useBasicInfoStore()

      const enchanting_list = computed<IEnchantingInfo[] | undefined>(() => {
        return basicInfoStore.enchanting_info?.filter(item => item.position.includes(detailsStore.part)).sort((a, b) => b.maxFrame - a.maxFrame)
      })

      const global_change = ref(true)

      const currentInfo = function <T>(name: string, defaultValue?: T) {
        return computed<string | number>({
          get() {
            return characterStore.getForge(detailsStore.part, name) ?? defaultValue
          },
          set(val) {
            if (global_change.value) {
              let parts: string[] = []
              switch (name) {
                case "enchanting":
                  const enchant = basicInfoStore.enchanting_info?.find(item => item.id == val) as IEnchantingInfo | undefined
                  console.log(enchant?.position.split("，"))
                  if (enchant?.position) {
                    parts = enchant.position.split("，")
                  }
                  break
                case "cursed_type":
                case "cursed_number":
                case "growth_First":
                case "growth_Second":
                case "growth_Fourth":
                case "growth_Second":
                  parts = detailsStore.display_parts.filter(e => !["称号", "宠物"].includes(e))
                  break
              }
              if (parts.length) {
                parts.forEach(e => characterStore.setForge(e, name, val))
              }
            }
            characterStore.setForge(detailsStore.part, name, val)
          }
        })
      }

      //附魔
      const enchanting = currentInfo<string | number>("enchanting", 0)

      // 镶嵌栏1
      const socket_left = currentInfo<string | number>("socket_left")

      // 镶嵌栏2
      const socket_right = currentInfo<string | number>("socket_right")

      // 增幅
      const cursed_type = currentInfo<string | number>("cursed_type", 0)

      const cursed_number = currentInfo<string | number>("cursed_number", 0)

      const wisdom_number = currentInfo<string | number>("wisdom_number", 0)

      const dz_number = currentInfo<string | number>("dz_number", 0)

      const growth_First = currentInfo<string | number>("growth_First", 1)

      const growth_Second = currentInfo<string | number>("growth_Second", 1)

      const growth_Third = currentInfo<string | number>("growth_Third", 1)

      const growth_Fourth = currentInfo<string | number>("dz_Fourth", 1)

      // function changeSocket(name: string, left: boolean = true) {
      //   const glc = global_change.value
      //   const socket_key = `socket_${left ? "left" : "right"}`
      //   let parts = [detailsStore.part]
      //   if (glc) {
      //     const emblem = characterStore.emblem_list.find(e => e.name == name)
      //     if (emblem) {
      //       parts.length = 0
      //       const colors = emblem.colors ?? []
      //       for (let color of colors) {
      //         const values = SocketMaps[color]
      //         parts.push(...values)
      //       }
      //     }
      //   }
      //   for (let part of parts) {
      //     if (glc) {
      //       characterStore.setColumnData(part, "socket_left", name)
      //       characterStore.setColumnData(part, "socket_right", name)
      //     } else {
      //       characterStore.setColumnData(part, socket_key, name)
      //     }
      //   }
      // }

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
                <calc-select v-model={socket_left.value} class="!h-20px flex-1"></calc-select>
                <calc-select v-model={socket_right.value} class="!h-20px flex-1"></calc-select>
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

<style lang="scss">
  .equ-profile {
    width: 100%;

    .equ-profile-item {
      width: 100%;
      height: 20px;
      display: flex;
      margin-top: 5px;
      margin-bottom: 5px;
      align-items: center;

      .row-name {
        flex: 0 0 50px;
        text-align: center;
      }

      :not(:last-child) {
        margin-right: 10px !important;
      }
    }
  }
</style>
