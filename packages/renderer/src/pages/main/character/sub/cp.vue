<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList } from "vue"
  import { useCharacterStore } from "@/store"

  import { skill_icon } from "./utils"
  export default defineComponent({
    name: "cp",
    components: {},

    setup(props, { emit, slots }) {
      // 红 绿
      const runeColor = ["#a128f4", "#a3240c", "#20f948", "#3aa8ff"]
      const characterStore = useCharacterStore()
      return () => (
        <div>
          <div class="head-sec">护石设置</div>
          <div class="body-sec">
            {renderList(3, item => (
              <div>
                <div class="cp">
                  <calc-iconselect class="talisman" emptyLabel="点击" columnNum={1}>
                    {renderList(characterStore.talisman, (talisman, index) => (
                      <calc-option value={talisman}>
                        <div>
                          <img src={skill_icon(characterStore.alter, talisman)} />
                        </div>
                      </calc-option>
                    ))}
                  </calc-iconselect>
                  {renderList([...Array(3).keys()], index => (
                    <calc-iconselect emptyLabel="点击" columnNum={4} class="rune">
                      {renderList(characterStore.rune, (rune, index) => (
                        <>
                          {renderList(runeColor.length, colorindex => (
                            <>
                              <calc-option value={index * 4 + colorindex - 1}>
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
    background-image: url(./images/common/talisman.png);
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
