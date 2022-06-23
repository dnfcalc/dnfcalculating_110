<script lang="tsx">
  import { ISkillInfo } from "@/api/character/type"
  import { SkillSet } from "@/api/info/type"
  import { useCharacterStore, useConfigStore } from "@/store"
  import { computed, defineComponent, reactive, renderList, watch } from "vue"
  import { skill_icon } from "./utils"

  function skill_tooltip(skill: ISkillInfo) {
    if (skill.type == 1)
      return (
        <div class="tooltip-skill">
          <div class="name">
            {skill.name} Lv {skill.current_level}
          </div>
          <div class="text-right info">冷却时间:{skill.cooldown}秒</div>
          <div class="info">学习等级:{+skill.need_level}</div>
          <div class="info">精通等级:{+skill.level_master}</div>
          <div class="info">上限等级:{+skill.level_max}</div>
          <div class="info">技能倍率:{+skill.data.toFixed(0)}%</div>
        </div>
      )
    else
      return (
        <div class="tooltip-skill">
          <div class="name-p">
            {skill.name} Lv {skill.current_level}
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
      const configStore = useConfigStore()

      const skills = reactive<SkillSet[]>([])
      characterStore.skills
        .sort((a, b) => a.need_level - b.need_level)
        .forEach(item => {
          const temp = configStore.getSkill(item.name)
          if (configStore.getSkill(item.name)) {
            skills.push(temp as SkillSet)
          } else {
            skills.push({ name: item.name, tp: 0, count: 0, pet: 0, direct: false, level: item.current_level, directNumber: 0, damage: item.type == 1, mode: item.mode })
          }
        })
      configStore.skill_set = skills

      function highlight(index: number) {
        if (skills[index].level > characterStore.skills[index].current_level) return "warn"
        if (skills[index].level < characterStore.skills[index].current_level) return "remind"
      }

      function skillTips(index: number) {
        const minus = skills[index].level - characterStore.skills[index].current_level
        if (minus != 0) {
          return `${minus > 0 ? "超出" : "低于"}标准Lv${Math.abs(minus)}`
        }
      }

      watch(skills, val => {
        configStore.skill_set = val
      })

      const skillQueChange = (count: number, skill: ISkillInfo) => {
        let indexs = (
          configStore.skill_que
            .map((item, index) => {
              if (item.name == skill.name) return index
            })
            .filter(item => item != undefined) ?? []
        ).sort((a, b) => (b ?? 0) - (a ?? 0))
        if (indexs.length > count) {
          // 删除后几位
          for (let i = 0; i < indexs.length - count; i++) {
            configStore.skill_que.splice(indexs[i] as number, 1)
          }
        } else {
          for (let i = 0; i < count - indexs.length; i++) {
            configStore.skill_que.push({ name: skill.name, id: 0, mode: skill.mode?.[0] ?? "", modes: skill.mode })
          }
        }
        configStore.skill_que = configStore.skill_que.map((item, index) => {
          item.id = index
          return item
        })
      }

      const wakens = computed(() => characterStore.skills.filter(item => item.need_level == 50 || item.need_level == 85))

      return () => (
        <div class="flex">
          {characterStore.is_delear && (
            <div class="flex-column">
              <div class="flex h-31px items-center">
                <div class="w-28px">技能</div>
                <div class="text-center w-50px !ml-10px">Lv</div>
                <div class="text-center w-50px !ml-5px">TP</div>
                {
                  <div class="text-center w-50px !ml-5px">次数</div>
                  // <div class="text-center w-50px !ml-5px">宠物次数</div>
                }
                <div class="text-center w-68px !ml-10px">手搓相关</div>
              </div>
              {renderList(
                characterStore.skills.sort((a, b) => a.need_level - b.need_level),
                (skill, index) =>
                  skill.type == 1 && (
                    <div class="flex mt-3px mb-3px items-center">
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
                      <calc-select v-model={skills[index].level} title={skillTips(index)} highlight={highlight(index)} class="!h-20px !ml-10px !min-w-45px !w-45px">
                        {renderList(skill.level_max + 1, item => (
                          <calc-option value={item - 1}>
                            <span>{item - 1}</span>
                          </calc-option>
                        ))}
                      </calc-select>
                      {(skill.tp_max as number) > 0 ? (
                        <calc-select v-model={skills[index].tp} class="!h-20px !ml-5px !min-w-45px !w-45px">
                          {renderList((skill.tp_max as number) + 1, item => (
                            <calc-option value={item - 1}>
                              <span>{item - 1}</span>
                            </calc-option>
                          ))}
                        </calc-select>
                      ) : (
                        <div class="!h-20px !ml-5px !w-50px"></div>
                      )}
                      {
                        <calc-select
                          v-model={skills[index].count}
                          onChange={(val: any) => {
                            skillQueChange(val, skill)
                          }}
                          class="!h-20px !ml-5px !min-w-45px !w-45px"
                        >
                          {renderList(100, item => (
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
                      <div class="w-20px justify-center !ml-5px">
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
          )}
          <div class="flex-column w-150px">
            <div class="h-31px"></div>
            {renderList(
              characterStore.skills,
              (skill, index) =>
                skill.type == 0 && (
                  <div class="flex mt-3px  mb-3px items-center justify-center">
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
                    <calc-select v-model={skills[index].level} highlight={highlight(index)} class={"!w-45px !min-w-45px !h-20px !ml-10px"}>
                      {renderList(skill.level_max + 1, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                  </div>
                )
            )}
            {characterStore.is_delear && (
              <div class="flex mt-20px items-center justify-center">
                <img src={skill_icon(characterStore.alter, "BUFF")} />
                <calc-autocomplete class="ml-10px !min-w-45px !w-50px" v-model={configStore.buff_ratio}></calc-autocomplete>
              </div>
            )}
            {
              // 由于技能队列的存在 暂时取消显示
              // <calc-selection v-model={buind_skill.value} class="flex flex-column mt-20px items-center justify-center">
              //   <calc-item value={wakens.value[0].name} class="h-50px w-38px" style="background-image:url('/images/common/waken.png');position:relative">
              //     {buind_skill.value == wakens.value[0].name ? <div></div> : <div class="waken"></div>}
              //     <img class="mt-3px ml-5px" src={skill_icon(characterStore.alter, wakens.value[0].name)} />
              //     <div class="text-center w-100%">1次</div>
              //   </calc-item>
              //   <calc-item value={wakens.value[1].name} class="h-50px ml-10px w-38px" style="background-image:url('/images/common/waken.png');position:relative">
              //     {buind_skill.value == wakens.value[1].name ? <div></div> : <div class="waken"></div>}
              //     <img class="mt-3px ml-5px" src={skill_icon(characterStore.alter, wakens.value[1].name)} />
              //     <div class="text-center w-100%">2次</div>
              //   </calc-item>
              // </calc-selection>
            }
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
