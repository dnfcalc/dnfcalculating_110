<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"
  import { useCharacterStore } from "@/store"
  import { ISkillInfo } from "@/api/character/type"
  import { SkillSet } from "@/api/info/type"
  import { skill_icon } from "./utils"

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
    name: "skill",
    components: {},
    setup(props, { emit, slots }) {
      const characterStore = useCharacterStore()

      const buind_skill = ref("EMP磁暴")

      const test = ref("0")

      const skills = reactive<SkillSet[]>([])
      characterStore.skillInfo.forEach(item => {
        const temp = characterStore.getSkill(item.name)
        if (characterStore.getSkill(item.name)) {
          skills.push(temp as SkillSet)
        } else {
          skills.push({ name: item.name, tp: 0, count: 0, pet: 0, direct: false, level: item.current_LV, directNumber: 0, damage: item.type == 1 })
        }
      })
      characterStore.skill_set = skills

      const highlight = computed(() => {
        return function (index: number) {
          if (skills[index].level > characterStore.skillInfo[index].current_LV) return "warn"
          if (skills[index].level < characterStore.skillInfo[index].current_LV) return "remind"
        }
      })

      watch(skills, val => {
        characterStore.skill_set = val
      })

      const wakens = computed(() => characterStore.skillInfo.filter(item => item.need_level == 50 || item.need_level == 85))

      return () => (
        <div class="flex">
          <div class="flex-column">
            <div class="flex items-center h-31px">
              <div class="w-28px"></div>
              <div class="w-50px !ml-10px text-center">Lv</div>
              <div class="w-50px !ml-5px text-center">TP</div>
              {
                <div class="w-50px !ml-5px text-center">次数</div>
                // <div class="w-50px !ml-5px text-center">宠物次数</div>
              }
              <div class="w-68px !ml-10px text-center">手搓相关</div>
            </div>
            {renderList(
              characterStore.skillInfo,
              (skill, index) =>
                skill.type == 1 && (
                  <div class="flex items-center">
                    <div>
                      <calc-tooltip position="right" offset={5}>
                        {{
                          default() {
                            return <img src={skill_icon(characterStore.alter, skill.name)} />
                          },
                          popper() {
                            return skill_tooltip(skill)
                          }
                        }}
                      </calc-tooltip>
                    </div>
                    <calc-select v-model={skills[index].level} highlight={highlight.value(index)} class="!w-45px !min-w-45px !h-20px !ml-10px">
                      {renderList(skill.level_max + 1, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                    {(skill.TP_max as number) > 0 ? (
                      <calc-select v-model={skills[index].tp} class="!w-45px !min-w-45px !h-20px !ml-5px">
                        {renderList((skill.TP_max as number) + 1, item => (
                          <calc-option value={item - 1}>
                            <span>{item - 1}</span>
                          </calc-option>
                        ))}
                      </calc-select>
                    ) : (
                      <div class="!w-50px !h-20px !ml-5px"></div>
                    )}
                    {
                      <calc-select v-model={skills[index].count} class="!w-45px !min-w-45px !h-20px !ml-5px">
                        {renderList(skill.level_max + 1, item => (
                          <calc-option value={item - 1}>
                            <span>{item - 1}</span>
                          </calc-option>
                        ))}
                      </calc-select>
                      // <calc-select editeable={true} v-model={skills[index].pet} class={"!w-45px !min-w-45px !h-20px !ml-5px !mr-5px"}>
                      //   {renderList(skill.level_max + 1, item => (
                      //     <calc-option value={item - 1}>
                      //       <span>{item - 1}</span>
                      //     </calc-option>
                      //   ))}
                      // </calc-select>
                    }
                    <div class="w-20px !ml-5px justify-center">
                      <calc-checkbox v-model={skills[index].direct}></calc-checkbox>
                    </div>

                    <calc-select v-model={skills[index].directNumber} disabled={!skills[index].direct} class={"!w-45px !min-w-45px !h-20px !mr-5px"}>
                      {renderList(5, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                  </div>
                )
            )}
          </div>
          <div class="flex-column w-150px">
            <div class="h-31px"></div>
            {renderList(
              characterStore.skillInfo,
              (skill, index) =>
                skill.type == 0 && (
                  <div class="flex items-center justify-center">
                    <div>
                      <calc-tooltip position="right" offset={5}>
                        {{
                          default() {
                            return <img src={skill_icon(characterStore.alter, skill.name)} />
                          },
                          popper() {
                            return skill_tooltip(skill)
                          }
                        }}
                      </calc-tooltip>
                    </div>
                    <calc-select v-model={skills[index].level} highlight={highlight.value(index)} class={"!w-45px !min-w-45px !h-20px !ml-10px"}>
                      {renderList(skill.level_max + 1, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                  </div>
                )
            )}
            <div class="flex items-center justify-center mt-20px">
              <img src={skill_icon(characterStore.alter, "BUFF")} />
              <calc-autocomplete class="!w-50px !min-w-45px ml-10px" v-model={test.value}></calc-autocomplete>
            </div>

            <div class="flex flex-column items-center justify-center mt-20px">
              <div onClick={() => (buind_skill.value = wakens.value[0].name)} class="h-50px w-38px" style="background-image:url('./images/common/waken.png');position:relative">
                {buind_skill.value == wakens.value[0].name ? <div></div> : <div class="waken"></div>}
                <img class="ml-5px mt-3px" src={skill_icon(characterStore.alter, wakens.value[0].name)} />
                <div class="w-100% text-center">1次</div>
              </div>
              <div onClick={() => (buind_skill.value = wakens.value[1].name)} class="h-50px w-38px ml-10px" style="background-image:url('./images/common/waken.png');position:relative">
                {buind_skill.value == wakens.value[1].name ? <div></div> : <div class="waken"></div>}
                <img class="ml-5px mt-3px" src={skill_icon(characterStore.alter, wakens.value[1].name)} />
                <div class="w-100% text-center">2次</div>
              </div>
            </div>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .waken::after {
    content: "";
    width: 38px;
    height: 50px;
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.4);
  }
</style>
