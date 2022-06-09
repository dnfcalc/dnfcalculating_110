<script lang="tsx">
  import { getSession, toMap, to_percent } from "@/utils"
  import { computed, defineComponent, ref, renderList } from "vue"
  import { useRoute } from "vue-router"
  import { useCharacterStore, useDetailsStore, useAppStore } from "@/store"
  import Profile from "@/components/internal/profile.vue"
  import { skill_icon } from "@/pages/main/character/sub/utils"
  import { IResultInfo } from "@/api/character/type"
  import api from "@/api"

  export default defineComponent({
    async setup() {
      const uid = (useRoute().query.res as string) ?? ""
      const standard = useRoute().query.standard
      const characterStore = useCharacterStore()
      const store = useDetailsStore()
      const appStore = useAppStore()
      console.log((useRoute().query.standard as string) ?? undefined)
      store.setStandard((useRoute().query.standard as string) ?? undefined)

      appStore.title = "详细数据"

      const res: IResultInfo = await api.getResult(uid)
      characterStore.$patch({ alter: res.alter, name: res.name })

      function skill_tooltip(skill: any) {
        return (
          <div class="tooltip-skill !p-5px !w-120px">
            <div class="info">等级:{+skill.lv}</div>
            <div class="info">MP消耗:{skill.mp.toFixed(0)}</div>
            <div class="info">无色消耗:{skill.无色}</div>
            <div class="info">百分比:{skill.百分比.toFixed(0) + "%"}</div>
          </div>
        )
      }

      const skillInfo = computed(() => {
        return (skill: string) => {
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

          return {
            cd: res.skills[skill].cd,
            count: res.skills[skill].count,
            damage: damage,
            avg: avg,
            mix: to_percent(res.skills[skill].damage / res.sumdamage, 0, "%")
          }
        }
      })

      return () => (
        <>
          <div class="flex h-100% m-0 detail" style="background: url('./images/common/bg.jpg') no-repeat;background-size:100% 100%">
            <div class="flex h-100% w-266px justify-center">
              <Profile sumdamage={res.sumdamage} equList={res.equips} class="!m-0 !p-0" details={res.info} standardSum={store.standard?.sumdamage}></Profile>
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
                  {renderList(Object.keys(res.skills) ?? [], item => (
                    <div class="flex justify-between">
                      <div class="w-12% item">
                        <div>
                          <calc-tooltip position="right">
                            {{
                              default() {
                                return <img src={skill_icon(characterStore.alter, item)} />
                              },
                              popper() {
                                return skill_tooltip(res.skills[item])
                              }
                            }}
                          </calc-tooltip>
                        </div>
                      </div>
                      <div class="w-12% item">{skillInfo.value(item).cd}</div>
                      <div class="w-12% item">{skillInfo.value(item).count}</div>
                      <div class="w-25% item" style={"color:" + skillInfo.value(item).damage[1]}>
                        {skillInfo.value(item).damage[0]}
                      </div>
                      <div class="w-25% item" style={"color:" + skillInfo.value(item).avg[1]}>
                        {skillInfo.value(item).avg[0]}
                      </div>
                      <div class="w-12% item">{to_percent(res.skills[item].damage / res.sumdamage, 0, "%")}</div>
                    </div>
                  ))}
                </div>
                <div class="bottom">被动详情</div>
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
