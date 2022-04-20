<script lang="tsx">
  import { useBasicInfoStore, useCharacterStore, useDetailsStore } from "@/store"
  import { computed, defineComponent, renderList, PropType } from "vue"
  import { IDetailInfo } from "../type"
  import { IEnchantingInfo } from "@/api/info/type"
  import { useVModel } from "@vueuse/core"
  import { log } from "console"
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

      const currentDetail = useVModel(props, "currentDetail", emit)

      //当前部位的附魔
      const enchanting = computed<string | number>({
        get() {
          return characterStore.getForge(detailsStore.part, "enchanting") ?? 0
        },
        set(val) {
          console.log(characterStore.forge_set, detailsStore.part, "enchanting", val)
          // console.log(val)
          // let parts = [detailsStore.part]
          characterStore.setForge(detailsStore.part, "enchanting", val)
          // if (global_change.value) {
          //   const enchant = characterStore.enchant_list.find(e => e.name == val) as Enchant
          //   if (enchant?.parts) {
          //     parts = enchant.parts
          //   }
          // }
          // for (let part of parts) {
          //   characterStore.setColumnData(part, "enchanting", val)
          // }
        }
      })

      return () => {
        if (currentDetail.value) {
          return (
            <div class="flex flex-wrap equ-profile">
              <div class="equ-profile-item">
                <div class="row-name mr-10px">当前部位</div>
                {detailsStore.part}
              </div>
              {can_upgrade.value ? (
                <div class="equ-profile-item">
                  <div class="row-name">增幅</div>
                  <calc-select class="!h-20px flex-1">
                    <calc-option value={1}>增幅</calc-option>
                    <calc-option value={2}>强化</calc-option>
                  </calc-select>
                  <calc-select class="!h-20px flex-1">
                    {renderList(32, i => (
                      <calc-option value={i}>{i}</calc-option>
                    ))}
                  </calc-select>
                  {has_wisdom.value ? (
                    <calc-select class="!h-20px flex-1">
                      {renderList(32, i => (
                        <calc-option value={i}>改造+ {i}</calc-option>
                      ))}
                    </calc-select>
                  ) : (
                    <calc-select class="!h-20px flex-1">
                      {renderList(9, i => (
                        <calc-option value={i}>锻造+ {i}</calc-option>
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
                  <calc-select class="!h-20px flex-1"></calc-select>
                  <calc-select class="!h-20px flex-1"></calc-select>
                </div>
              ) : (
                <div></div>
              )}
              {can_upgrade.value ? (
                <div class="equ-profile-item">
                  <div class="row-name">成长属性</div>
                  <calc-select class="!h-20px flex-1">
                    {renderList(100, i => (
                      <calc-option value={i + 1}>属性1 Lv{i + 1}</calc-option>
                    ))}
                  </calc-select>
                  <calc-select class="!h-20px flex-1">
                    {renderList(100, i => (
                      <calc-option value={i + 1}>属性2 Lv{i + 1}</calc-option>
                    ))}
                  </calc-select>
                  <calc-select class="!h-20px flex-1">
                    {renderList(100, i => (
                      <calc-option value={i + 1}>属性3 Lv{i + 1}</calc-option>
                    ))}
                  </calc-select>
                  <calc-select class="!h-20px flex-1">
                    {renderList(100, i => (
                      <calc-option value={i + 1}>属性4 Lv{i + 1}</calc-option>
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
      return <div></div>
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
      align-items: baseline;
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
