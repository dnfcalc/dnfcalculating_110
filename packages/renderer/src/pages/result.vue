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
    cd: number
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

      const res = toMap(await api.getResult(uid), ["info", "skills", "skills_passive"]) as IResultInfo
      characterStore.$patch({ alter: res.alter, name: res.name })
      configStore.forge_set = res.forget_set ?? {}
      function skill_tooltip(skill: any) {
        const skllInfo = res.skills[skill]
        return (
          <div class="tooltip-skill">
            <div class="name">
              {skill} Lv {skllInfo.lv}
            </div>
            <div class="text-right info">冷却时间:{skllInfo.cd}秒</div>
            <div class="info">MP消耗:{skllInfo.mp.toFixed(0)}</div>
            <div class="info">无色消耗:{skllInfo.无色}</div>
            <div class="info">百分比:{skllInfo.百分比.toFixed(0) + "%"}</div>
          </div>
        )
      }

      function skill_passive_tooltip(skill: ISkillPassive) {
        return (
          <div class="tooltip-skill">
            <div class="name">
              {skill.name} Lv {skill.lv}
            </div>
            {renderList(skill.info, item => (
              <>
                <div class="info">
                  {item.type}:{item.info[0]}%<div></div>
                </div>
                <div class="info">
                  关联技能:{item.info[1]}
                  {item.info[2] != "无" && item.info[2] != "" && <div class="text-hex-696969">({item.info[2]}除外)</div>}
                </div>
              </>
            ))}
          </div>
        )
      }

      const skills = computed(() => {
        let temp: ISkillResult[] = []
        Object.keys(res.skills).forEach(skill => {
          let damage = ["", "white"]
          let avg = []
          if (store.standard?.skills[skill]?.damage ?? undefined) {
            if (store.standard?.skills[skill].damage == res.skills[skill].damage) damage = ["无变化", "white"]
            else
              damage = [
                to_percent(res.skills[skill].damage / store.standard?.skills[skill].damage - 1, 0, "%", true),
                res.skills[skill].damage > store.standard?.skills[skill].damage ? "#3ea74e" : "red"
              ]
          } else {
            damage = [Math.round(res.skills[skill].damage).toLocaleString(), "white"]
          }

          if (store.standard?.skills[skill]?.damage ?? undefined) {
            if (store.standard?.skills[skill].damage / store.standard?.skills[skill].count == res.skills[skill].damage / res.skills[skill].count) avg = ["无变化", "white"]
            else
              avg = [
                to_percent(res.skills[skill].damage / res.skills[skill].count / (store.standard?.skills[skill].damage / store.standard?.skills[skill].count) - 1, 0, "%", true),
                res.skills[skill].damage / res.skills[skill].count > store.standard?.skills[skill].damage / store.standard?.skills[skill].count ? "#3ea74e" : "red"
              ]
          } else {
            avg = [Math.round(res.skills[skill].damage / res.skills[skill].count).toLocaleString(), "white"]
          }
          temp.push({
            name: skill,
            cd: res.skills[skill].cd,
            count: res.skills[skill].count,
            damage: damage,
            avg: avg,
            mix: to_percent(res.skills[skill].damage / res.total_data, 0, "%"),
            order: res.skills[skill].damage
          })
        })
        temp.sort((a, b) => b.order - a.order)
        return temp
      })

      const skill_passive = computed(() => {
        let temp: ISkillPassive[] = []
        Object.keys(res.skills_passive).forEach(name => {
          let skill = res.skills_passive[name]
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

      return () => (
        <>
          <div class="flex h-100% m-0 detail" style="background: url('./images/common/bg.jpg') no-repeat;background-size:100% 100%">
            <div class="flex h-100% w-266px justify-center">
              <Profile total-data={res.total_data} equList={res.equips} class="!m-0 !p-0" details={res.info} standardSum={store.standard?.total_data}></Profile>
            </div>
            <div class="bg-hex-000000/60 flex-1 ml-1px pt-10px pr-15px pb-10px pl-15px" style="border:1px solid rgba(255,255,255,0.15)">
              <div class="flex flex-col bg-hex-000000/40 h-100% text-hex-FFFFFF w-100%" style="border:1px solid rgba(255,255,255,0.15)">
                <div class="bg-black flex h-15px justify-between !text-hex-B2966B">
                  <div class="w-12% item-head">技能</div>
                  <div class="w-12% item-head">CD</div>
                  <div class="w-12% item-head">次数</div>
                  <div class="w-25% item-head">总伤害</div>
                  <div class="w-25% item-head">平均伤害</div>
                  <div class="w-12% item-head">占比</div>
                </div>
                <div class="flex flex-col flex-1 skills">
                  {renderList(skills.value ?? [], skill => (
                    <div class="flex justify-between">
                      <div class="w-12% item">
                        <div>
                          <calc-tooltip position="right">
                            {{
                              default() {
                                return <img src={skill_icon(characterStore.alter, skill.name)} />
                              },
                              popper() {
                                return skill_tooltip(skill.name)
                              }
                            }}
                          </calc-tooltip>
                        </div>
                      </div>
                      <div class="w-12% item">{skill.cd}s</div>
                      <div class="w-12% item">{skill.count}</div>
                      <div class="w-25% item" style={"color:" + skill.damage[1]}>
                        {skill.damage[0]}
                      </div>
                      <div class="w-25% item" style={"color:" + skill.avg[1]}>
                        {skill.avg[0]}
                      </div>
                      <div class="w-12% item">{to_percent(skill.order / res.total_data, 0, "%")}</div>
                    </div>
                  ))}
                </div>
                <div class="flex bottom items-center">
                  {renderList(skill_passive.value, skill => (
                    <div class="mr-5px">
                      <calc-tooltip position="top">
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
              </div>
            </div>
          </div>
        </>
      )
    }
  })
</script>

<style lang="scss">
  .detail {
    .item-head {
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(#2b2817, #171407);
      // font-size: 12px;
      height: 14px;
      border-top: 1px solid #423d2c;
      border-bottom: 1px solid #211d15;
    }

    .skills {
      overflow-y: auto;
      .item {
        display: flex;
        justify-content: center;
        align-items: center;
        // font-size: 12px;
        height: 35px;
        // border-top: 1px solid white;
        // border-bottom: 1px solid white;
      }
    }

    .bottom {
      margin-left: 5px;
      margin-right: 5px;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
      height: 30px;
      margin-bottom: 5px;
    }
  }
</style>
