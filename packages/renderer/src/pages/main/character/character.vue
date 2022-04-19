<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList } from "vue"
  import { useCharacterStore } from "@/store"
  import { ISkillInfo } from "@/api/character/type"
  import Profile from "./profile.vue"

  function skill_tooltip(skill: ISkillInfo) {
    if (skill.type == 1)
      return (
        <div class="tooltip-skill">
          <div class="name">
            {skill.name} Lv {skill.current_LV}
          </div>
          <div class="info text-right">冷却时间:{skill.CD}秒</div>
          <div class="info">学习等级:{+skill.need_level}</div>
          <div class="info">精通等级:{+skill.level_master}</div>
          <div class="info">上限等级:{+skill.level_max}</div>
          <div class="info">技能倍率:{+skill.data}%</div>
        </div>
      )
    else
      return (
        <div class="tooltip-skill">
          <div class="name-p">
            {skill.name} Lv {skill.current_LV}
          </div>
          <div class="info">学习等级:{+skill.need_level}</div>
          <div class="info">精通等级:{+skill.level_master}</div>
          <div class="info">上限等级:{+skill.level_max}</div>
        </div>
      )
  }

  export default defineComponent({
    components: {},
    setup() {
      let test = ref(0)

      const characterStore = useCharacterStore()

      const detail = {
        mingwang: "20,660"
      }

      const visible = ref(false)
      // 红 绿
      const runeColor = ["#a128f4", "#a3240c", "#20f948", "#3aa8ff"]

      function skill_icon(skillName: string) {
        return `./images/characters/${characterStore.alter}/skill/${skillName}.png`
      }

      return () => (
        <div class="character flex">
          <div class="flex w-30%">
            <div class="flex-column">
              {renderList(characterStore.skillInfo, skill => (
                <div>
                  <calc-tooltip position="right" offset={5}>
                    {{
                      default() {
                        return <img src={skill_icon(skill.name)} />
                      },
                      popper() {
                        return skill_tooltip(skill)
                      }
                    }}
                  </calc-tooltip>
                </div>
              ))}
            </div>
          </div>
          <div>
            <div class="h-30% subitem mt-2%">
              <div class="head-sec">护石设置</div>
              <div class="body-sec">
                {renderList([...Array(3).keys()], item => (
                  <div>
                    <div class="cp">
                      <calc-iconselect class="talisman" emptyLabel="点击" modelValue={-1}>
                        {renderList(characterStore.talisman, (talisman, index) => (
                          <calc-option value={0}>
                            <img src={skill_icon(talisman)} />
                          </calc-option>
                        ))}
                      </calc-iconselect>
                      {renderList([...Array(3).keys()], index => (
                        <calc-iconselect emptyLabel="点击" v-model:modelValue={test.value} columnNum={4} class="rune">
                          {renderList(characterStore.rune, (rune, index) => (
                            <>
                              {renderList([...Array(runeColor.length).keys()], colorindex => (
                                <>
                                  <calc-option value={index * 4 + colorindex}>
                                    <div style={"background-color: " + runeColor[colorindex] + "; width:28px;height:28px"}>
                                      <img style="mix-blend-mode: luminosity;" src={skill_icon(rune)} />
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
            <div class="h-50% skill-slots subitem mt-2%">
              <div class="head-sec">技能快捷键设置</div>
              <div class="body-sec">
                <div class="flex flex-row ml-2 mr-2">
                  <div class="skill-slot-item">
                    <img src={`./images/characters/${characterStore.alter}/skill/交叉射击.png`} />
                  </div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                </div>
                <div class="flex flex-row ml-2 mr-2 mt-2">
                  <div class="skill-slot-item">
                    <img src={`./images/characters/${characterStore.alter}/skill/交叉射击.png`} />
                  </div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                  <div class="skill-slot-item"></div>
                </div>
              </div>
            </div>
            <div class="h-20%">职业个性化部分</div>
          </div>
          <div>
            <Profile charName={characterStore.alter} details={detail} charType="魔法固伤" />
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
  .skill-slot-item {
    height: 28px;
    width: 28px;
    background-color: black;
    border: rgb(29, 29, 29) solid 1px;
    margin: 1px;
  }
</style>
