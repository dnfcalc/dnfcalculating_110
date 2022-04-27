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

      let set: SkillSet[] = []

      characterStore.skillInfo.forEach(item => {
        const temp = characterStore.getSkill(item.name)
        if (characterStore.getSkill(item.name)) {
          set.push(temp as SkillSet)
        } else {
          set.push({ name: item.name, tp: 0, count: 0, pet: 0, direct: false, level: item.current_LV, directNumber: 0 })
        }
      })

      const skills = reactive<SkillSet[]>(set)
      const highlight = computed(() => {
        return function (index: number) {
          if (skills[index].level > characterStore.skillInfo[index].current_LV) return "warn"
          if (skills[index].level < characterStore.skillInfo[index].current_LV) return "remind"
        }
      })

      watch(skills, val => {
        characterStore.skill_set = val
      })

      return () => (
        <div class="flex">
          <div class="flex-column">
            <div class="flex items-center h-31px">
              <div class="w-28px"></div>
              <div class="w-48px !ml-5px text-center">Lv</div>
              <div class="w-48px !ml-5px text-center">TP</div>
              <div class="w-48px !ml-5px text-center">次数</div>
              <div class="w-48px !ml-5px text-center">宠物次数</div>
              <div class="w-30px !ml-5px text-center">手搓</div>
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
                    <calc-select v-model={skills[index].level} highlight={highlight.value(index)} class="!w-45px !min-w-45px !h-20px !ml-5px">
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
                      <div class="!w-48px !h-20px !ml-5px"></div>
                    )}
                    <calc-select v-model={skills[index].count} class="!w-45px !min-w-45px !h-20px !ml-5px">
                      {renderList(skill.level_max + 1, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                    <calc-select editeable={true} v-model={skills[index].pet} class={"!w-45px !min-w-45px !h-20px !ml-5px !mr-5px"}>
                      {renderList(skill.level_max + 1, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                    <div class="w-30px !ml-5px justify-center">
                      <calc-checkbox v-model={skills[index].direct}></calc-checkbox>
                    </div>
                  </div>
                )
            )}
          </div>
          <div class="flex-column">
            {renderList(
              characterStore.skillInfo,
              (skill, index) =>
                skill.type == 0 && (
                  <div class="flex">
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
                    <calc-select v-model={skills[index].level} highlight={highlight.value(index)} class={"!w-45px !min-w-45px !h-20px"}>
                      {renderList(skill.level_max + 1, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                  </div>
                )
            )}
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss"></style>
