<script lang="tsx">
  import { getSession, toMap, to_percent } from "@/utils"
  import { defineComponent, ref, renderList } from "vue"
  import { useRoute } from "vue-router"
  import { useCharacterStore, useConfigStore, useAppStore } from "@/store"
  import profile from "@/components/internal/profile.vue"
  import { skill_icon } from "@/pages/main/character/sub/utils"

  export default defineComponent({
    components: { profile },
    async setup() {
      const uid = (useRoute().query.uid as string) ?? ""
      const configStore = useConfigStore()
      const characterStore = useCharacterStore()
      let data: any = await getSession(uid)
      const res = data.res
      configStore.forge_set = (toMap({ forge_set: data.forge_set }) as { forge_set: any }).forge_set
      characterStore.alter = data.alter
      characterStore.name = data.name
      useAppStore().title = "详细数据"

      function skill_tooltip(skill: any) {
        return (
          <div class="tooltip-skill">
            <div class="info">MP消耗:{skill.mp}</div>
            <div class="info">无色消耗:{skill.无色}</div>
            <div class="info">等级:{+skill.lv}</div>
          </div>
        )
      }

      return () => (
        <>
          <div class="m-0 flex h-100% detail" style="background: url('./images/common/bg.jpg') no-repeat;background-size:100% 100%">
            <div class="h-100% w-266px flex justify-center">{<profile class="!m-0 !p-0" details={res.info}></profile>}</div>
            <div class="flex-1 bg-hex-000000/60 ml-1px pl-15px pr-15px pt-10px pb-10px" style="border:1px solid rgba(255,255,255,0.15)">
              <div class="w-100% h-100% bg-hex-000000/40 text-hex-FFFFFF flex flex-col" style="border:1px solid rgba(255,255,255,0.15)">
                <div class="h-15px bg-black flex justify-between !text-hex-B2966B">
                  <div class="item-head w-12%">技能</div>
                  <div class="item-head w-12%">CD</div>
                  <div class="item-head w-12%">次数</div>
                  <div class="item-head w-25%">总伤害</div>
                  <div class="item-head w-25%">平均伤害</div>
                  <div class="item-head w-12%">占比</div>
                </div>
                <div class="skills flex flex-col flex-1">
                  {renderList(Object.keys(res.skills) ?? [], item => (
                    <div class="flex justify-between">
                      <div class="item w-12%">
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
                      <div class="item w-12%">{res.skills[item].cd}</div>
                      <div class="item w-12%">{res.skills[item].count}</div>
                      <div class="item w-25%">{Math.round(res.skills[item].damage).toLocaleString()}</div>
                      <div class="item w-25%">{Math.round(res.skills[item].damage / res.skills[item].count).toLocaleString()}</div>
                      <div class="item w-12%">{to_percent(res.skills[item].damage / res.sumdamage, 0, "%")}</div>
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
