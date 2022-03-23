<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, reactive } from "vue"
  import { useCharacterStore } from "@/store"
  import { ICharacterInfo, ISkillInfo } from "@/api/character/type"
  import { useRoute } from "vue-router"
  import router from "@/router"

  function skill_icon(character: string, skillName: string) {
    return `./images/characters/${character}/skill/${skillName}.png`
  }

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

  export default defineComponent(() => {
    let basicInfo = ref<ICharacterInfo>({ skillInfo: [], individuation: [] })
    let characterName = ref<string>("")
    const route = useRoute()
    if (typeof route.params.name === "string")
      characterName.value = route.params.name
    onMounted(async () => {
      const characterInfoState = useCharacterStore()
      await characterInfoState.get_character_info(characterName.value)
      basicInfo.value = characterInfoState[characterName.value]
        ?.basicInfo as ICharacterInfo
    })

    const visible = ref(false)
    const showDialog = () => (visible.value = true)

    return () => (
      <div class="character flex">
        <div class="flex w-30%">
          <div class="flex-column">
            {renderList(basicInfo.value.skillInfo, (skill, index) => (
              <div>
                <calc-tooltip position="right" offset={5}>
                  {{
                    default() {
                      return (
                        <img
                          src={skill_icon(characterName.value, skill.name)}
                        />
                      )
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
                <div class="cp">
                  <calc-iconselect
                    class="hushi"
                    emptyLabel="点击"
                    modelValue={-1}
                  >
                    {renderList(basicInfo.value.hushi, (hushi, index) => (
                      <div>
                        <calc-option value={0}>
                          <img
                            src={skill_icon(characterName.value, hushi)}
                            // style="filter: sepia(100%);"
                          />
                        </calc-option>
                      </div>
                    ))}
                  </calc-iconselect>
                </div>
              ))}
            </div>
          </div>
          <div class="h-50% skill-slots subitem mt-2%">
            <div class="head-sec">技能快捷键设置</div>
            <div class="body-sec">
              <div class="flex flex-row ml-2 mr-2">
                <div class="skill-slot-item">
                  <img src="./images/characters/重霄·弹药专家·女/skill/交叉射击.png" />
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
                  <img src="./images/characters/重霄·弹药专家·女/skill/交叉射击.png" />
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
      </div>
    )
  })
</script>

<style lang="scss">
  .character {
    background-color: gray;
  }

  .cp {
    background-image: url(./images/common/hushi.png);
    height: 52px;
    width: 168px;
    margin: 0 auto;
    margin-top: 5px;
    .hushi {
      position: relative;
      top: 11px;
      left: 9px;
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
