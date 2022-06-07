<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList } from "vue"
  import { useCharacterStore, useConfigStore } from "@/store"

  import { skill_icon } from "./utils"
  export default defineComponent({
    name: "cp",
    components: {},

    setup(props, { emit, slots }) {
      //紫 红 绿 蓝
      const runeColor = ["#a128f4", "#a3240c", "#20f948", "#3aa8ff"]
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()

      const talismanList = computed(() => {
        return (index: number) => {
          return characterStore.talisman?.filter(a => configStore.talisman_set.filter((b, c) => c != index).indexOf(a) < 0)
        }
      })
      return () => (
        <div>
          <div class="head-sec">护石设置</div>
          <div class="body-sec">
            {renderList(3, item => (
              <div>
                <div class="cp" style="background-image: url('/images/common/talisman.png')">
                  <calc-iconselect class="talisman" emptyLabel="点击" columnNum={1} v-model={configStore.talisman_set[item - 1]}>
                    {renderList(talismanList.value(item - 1), (talisman, index) => (
                      <calc-option value={talisman}>
                        <div>
                          <img src={skill_icon(characterStore.alter, talisman)} />
                        </div>
                      </calc-option>
                    ))}
                  </calc-iconselect>
                  {renderList(3, runeItem => (
                    <calc-iconselect emptyLabel="点击" columnNum={4} class="rune" v-model={configStore.rune_set[(item - 1) * 3 + runeItem - 1]}>
                      {renderList(characterStore.rune, (rune, index) => (
                        <>
                          {renderList(runeColor.length, colorindex => (
                            <>
                              <calc-option value={rune + colorindex}>
                                <div style={"background-color: " + runeColor[colorindex - 1] + "; width:28px;height:28px"}>
                                  <img style="mix-blend-mode: luminosity;" src={skill_icon(characterStore.alter, rune)} />
                                </div>
                              </calc-option>
                            </>
                          ))}
                        </>
                      ))}
                    </calc-iconselect>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .cp {
    height: 52px;
    width: 168px;
    margin: 0 auto;
    margin-top: 5px;
    display: flex;
    .talisman {
      width: 28px;
      margin-left: 9px;
      margin-top: 11px;
    }
    .rune {
      width: 28px;
      margin-left: 5px;
      margin-top: 12px;
    }
    .rune:nth-child(2) {
      margin-left: 21px;
    }
  }
</style>
