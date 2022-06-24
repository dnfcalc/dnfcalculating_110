<script lang="tsx">
  import api from "@/api"
  import { IResultInfo } from "@/api/character/type"
  import Profile from "@/components/internal/profile.vue"
  import { skill_icon } from "@/pages/main/character/sub/utils"
  import { useAppStore, useCharacterStore, useConfigStore, useDetailsStore } from "@/store"
  import { toMap, to_percent } from "@/utils"
  import { computed, defineComponent, renderList } from "vue"
  import { useRoute } from "vue-router"

  interface ISkillResult {
    cd?: number
    count: number
    damage: string[]
    avg: string[]
    mix: string
    order: number
    name: string
  }

  interface ISkillPassive {
    lv: number
    name: string
    info: {
      type: string
      info: (string | number)[]
      percent?: boolean
    }[]
  }

  export default defineComponent({
    async setup() {
      const uid = (useRoute().query.res as string) ?? ""
      const standard = useRoute().query.standard
      const characterStore = useCharacterStore()
      const store = useDetailsStore()
      const appStore = useAppStore()
      const configStore = useConfigStore()

      store.setStandard((useRoute().query.standard as string) ?? undefined)

      appStore.title = "详细数据"

      const res = toMap(await api.getResult(uid), ["info", "skills", "skills_passive"]) as IResultInfo<"buffer"> | IResultInfo<"delear">
      characterStore.$patch({ alter: res.alter, name: res.name })
      configStore.forge_set = res.forget_set ?? {}
      function skill_tooltip(skill: string) {
        if (res.role == "buffer") {
          return <div></div>
        }
        const delearSkills = res.skills[skill]
        return (
          <div class="tooltip-skill">
            <div class="name">
              {skill} Lv {delearSkills.level}
            </div>
            <div class=" info">冷却时间:{delearSkills.cd}秒</div>
            <div class="info">MP消耗:{delearSkills.mp?.toFixed(0)}</div>
            <div class="info">无色消耗:{delearSkills.cosume_cube_frag}</div>
            <div class="info">百分比:{delearSkills.rate?.toFixed(0) + "%"}</div>
          </div>
        )
      }

      function transformNum(num = 0, digit = 0) {
        return num <= 0 ? "-" : num.round(digit).toLocaleString()
      }

      function skill_passive_tooltip(skill: ISkillPassive) {
        return (
          <div class="tooltip-skill">
            <div class="name">
              {skill.name} Lv {skill.lv}
            </div>
            {renderList(skill.info, item => {
              const percent = item.percent ?? true
              return (
                <>
                  <div class="info">
                    {item.type}:{item.info[0]}
                    {percent && "%"}
                    <div></div>
                  </div>
                  <div class="info">
                    关联技能:{item.info[1]}
                    {item.info[2] != "无" && item.info[2] != "" && item.info[2] != 0 && <div class="text-hex-696969">({item.info[2]}除外)</div>}
                  </div>
                </>
              )
            })}
          </div>
        )
      }

      function renderSkills() {
        if (res.role == "buffer") {
          return renderList(Object.values(res.skills), skill => {
            return (
              <tr>
                <td width="12%" class=" h-9 leading-9">
                  <calc-tooltip class="flex justify-center" position="right">
                    {{
                      default() {
                        return <img src={skill_icon(characterStore.alter, skill.name)} />
                      },
                      popper() {
                        return skill_tooltip(skill.name)
                      }
                    }}
                  </calc-tooltip>
                </td>
                <td width="12%">{skill.level}</td>
                <td width="16%">{transformNum(skill.data[0])}</td>
                <td width="16%">{transformNum(skill.data[1])}</td>
              </tr>
            )
          })
        }
        let temp: ISkillResult[] = []

        Object.keys(res.skills).forEach(skill => {
          let display_damage = ["", "white"]
          let avg = []
          const standard_skill = store.standard?.skiils[skill] as typeof res.skills[string]
          const standard_damage = standard_skill?.damage as number

          const current_damage = res.skills[skill].damage

          if (standard_damage) {
            if (standard_damage == current_damage) {
              display_damage = ["无变化", "white"]
            } else {
              display_damage = [to_percent(current_damage / standard_damage - 1, 0, "%", true), current_damage > standard_damage ? "#3ea74e" : "red"]
            }
          } else {
            display_damage = [Math.round(current_damage).toLocaleString(), "white"]
          }

          if (standard_damage) {
            if (standard_damage / store.standard?.skills[skill].count == res.skills[skill].damage / res.skills[skill].count) {
              avg = ["无变化", "white"]
            } else {
              avg = [
                to_percent(res.skills[skill].damage / res.skills[skill].count / (store.standard?.skills[skill].damage / store.standard?.skills[skill].count) - 1, 0, "%", true),
                res.skills[skill].damage / res.skills[skill].count > store.standard?.skills[skill].damage / store.standard?.skills[skill].count ? "#3ea74e" : "red"
              ]
            }
          } else {
            avg = [Math.round(res.skills[skill].damage / res.skills[skill].count).toLocaleString(), "white"]
          }
          temp.push({
            name: skill,
            cd: res.skills[skill].cd,
            count: res.skills[skill].count,
            damage: display_damage,
            avg: avg,
            mix: to_percent(res.skills[skill].damage / res.total_data[0], 0, "%"),
            order: res.skills[skill].damage
          })
        })
        temp.sort((a, b) => b.order - a.order)
        return renderList(temp, skill => (
          <tr>
            <td width="12%" class=" h-9 leading-9">
              <calc-tooltip class="flex justify-center" position="right">
                {{
                  default() {
                    return <img src={skill_icon(characterStore.alter, skill.name)} />
                  },
                  popper() {
                    return skill_tooltip(skill.name)
                  }
                }}
              </calc-tooltip>
            </td>
            <td width="12%" class="h-9 text-center leading-9">
              {skill.cd}s
            </td>
            <td width="12%" class="h-9 text-center leading-9">
              {skill.count}
            </td>
            <td width="24%" class="h-9  leading-9" style={"color:" + skill.damage[1]}>
              {skill.damage[0]}
            </td>
            <td width="24%" class="h-9  leading-9" style={"color:" + skill.avg[1]}>
              {skill.avg[0]}
            </td>
            <td width="14%" class="h-9  pr-2 leading-9">
              {to_percent(skill.order / res.total_data[0], 0, "%")}
            </td>
          </tr>
        ))
      }

      const skill_passive = computed(() => {
        let temp: ISkillPassive[] = []
        Object.keys(res.skills_passive).forEach(name => {
          let skill = res.skills_passive[name]
          console.log(skill.info)
          //   console.log(res.skills_passive[name])
          if (skill.info.length > 0) {
            temp.push({
              name: name,
              lv: skill.lv,
              info: skill.info
            })
          }
        })
        return temp
      })

      const headers = computed(() => {
        if (res.role == "delear") {
          return [
            {
              title: "技能",
              width: "12%"
            },
            {
              title: "CD",
              width: "12%"
            },
            {
              title: "次数",
              width: "12%"
            },
            {
              title: "总伤害",
              width: "24%"
            },
            {
              title: "平均伤害",
              width: "24%"
            },
            {
              title: "伤害占比",
              width: "14%"
            }
          ]
        } else {
          return [
            {
              title: "技能",
              width: "12%"
            },
            {
              title: "等级",
              width: "12%"
            },
            {
              title: "力智",
              width: "16%"
            },
            {
              title: "三攻",
              width: "16%"
            }
          ]
        }
      })

      return () => (
        <>
          <div class="flex h-full m-0 overflow-hidden detail" style="background: url('./images/common/bg.jpg') no-repeat;background-size:cover">
            <div class="flex h-full w-266px justify-center">
              <Profile total-data={res.total_data} role={res.role} equList={res.equips} class="!m-0 !p-0" details={res.info} standardSum={store.standard?.total_data}></Profile>
            </div>
            <table class="h-full bg-hex-000000/60 flex-1 ml-1 p-4 block overflow-y-hidden " style="border:1px solid rgba(255,255,255,0.15)">
              <thead class="bg-hex-000000/40 text-white w-full" style="border:1px solid rgba(255,255,255,0.15)">
                <tr class="bg-black h-4 !text-hex-B2966B">
                  {renderList(headers.value, head => {
                    return <th width={head.width}>{head.title}</th>
                  })}
                </tr>
              </thead>

              <tbody class="text-white skills overflow-y-auto block" style="height:calc(100% - 96px)">
                {renderSkills()}
              </tbody>
              <div class="flex h-8  p-1 items-center">
                {renderList(skill_passive.value, skill => (
                  <div class="mr-1">
                    <calc-tooltip z={9} position="top">
                      {{
                        default() {
                          return <img src={skill_icon(characterStore.alter, skill.name)} />
                        },
                        popper() {
                          return skill_passive_tooltip(skill)
                        }
                      }}
                    </calc-tooltip>
                  </div>
                ))}
              </div>
              <tr class="bottom h-8 w-full p-1 block"></tr>
            </table>
          </div>
        </>
      )
    }
  })
</script>

<style lang="scss" scoped>
  table thead,
  tbody tr {
    display: table;
    width: 100%;
    table-layout: fixed;

    td {
      text-align: center;
    }
  }
  .detail {
    .item-head {
      background: linear-gradient(#2b2817, #171407);
      // font-size: 12px;
      border-top: 1px solid #423d2c;
      border-bottom: 1px solid #211d15;
    }

    .bottom {
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    }
  }
</style>
