<script lang="tsx">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  import { useCharacterStore, useConfigStore } from "@/store"
  import { useAppStore } from "@/store/app"
  import { useOpenWindow } from "@/hooks/open"
  import { defineComponent, ref, renderList } from "vue"
  import { useRoute } from "vue-router"

  import Character from "@/pages/main/character/character.vue"
  import Customize from "@/pages/main/customize/customize.vue"
  import Equipment from "@/pages/main/equipment/equipment.vue"
  import Detail from "@/pages/main/detail/detail.vue"
  import Singleset from "@/pages/main/singleset/singleset.vue"

  export default defineComponent(() => {
    const route = useRoute()
    const tab = ref(0)
    const char = route.query.name as string
    const appStore = useAppStore()
    const configStore = useConfigStore()
    const characterStore = useCharacterStore()

    characterStore.newCharacter(char).then(() => {
      appStore.$patch({ title: characterStore.name })
    })

    const openResult = useOpenWindow()

    async function calc() {
      // alert({
      //   content: () => <>暂不支持多套计算</>
      // })
      // return
      // 一堆前处理和判断，然后计算
      const saveData = await configStore.calc(route.path.endsWith("/singleset"))
      if (saveData instanceof Array) {
        // 排行界面
        openResult({ url: "/ranking?uid=" + saveData.id, width: 800, height: 800 })
      } else if (saveData) {
        // 详情界面
        openResult({ url: `/result?res=${saveData.id}`, width: 890, height: 600 })
      }
    }

    return () => {
      if (characterStore.alter) {
        return (
          <div class="main" style={"background-image:url(/images/characters/" + characterStore.alter + "/bg.jpg)"}>
            {
              //               <div class="header">
              //   <calc-tabs route>
              //     <calc-tab value={"/character/equips?name=" + characterStore.alter}>装备</calc-tab>
              //     <calc-tab value={"/character/skills?name=" + characterStore.alter}>技能</calc-tab>
              //     <calc-tab value={"/character/profile?name=" + characterStore.alter}>打造</calc-tab>
              //     <calc-tab value={"/character/customize?name=" + characterStore.alter}>自选属性</calc-tab>
              //     <calc-tab value={"/character/singleset?name=" + characterStore.alter}>单套选择</calc-tab>
              //   </calc-tabs>
              // </div>
              // <div class="center">{characterStore.alter && <router-view></router-view>}</div>
            }

            <div class="header">
              <calc-tabs v-model={tab.value}>
                <calc-tab value={0}>装备</calc-tab>
                <calc-tab value={1}>技能</calc-tab>
                <calc-tab value={2}>打造</calc-tab>
                <calc-tab value={3}>自选属性</calc-tab>
                <calc-tab value={4}>单套选择</calc-tab>
              </calc-tabs>
            </div>
            <div class="center">
              {characterStore.alter && (
                <>
                  {tab.value == 0 && <Equipment style={tab.value == 0 ? "" : "display:none"}></Equipment>}
                  <Character style={tab.value == 1 ? "" : "display:none"}></Character>
                  <Detail style={tab.value == 2 ? "" : "display:none"}></Detail>
                  <Customize style={tab.value == 3 ? "" : "display:none"}></Customize>
                  <Singleset style={tab.value == 4 ? "" : "display:none"}></Singleset>
                </>
              )}
            </div>
            <div class="footer">
              <div class="flex col-4 justify-center">
                <calc-select v-model={configStore.carry_type} class="!h-22px">
                  {renderList(characterStore.carry_type_list, (item, index) => (
                    <calc-option value={item}>{item}</calc-option>
                  ))}
                </calc-select>
              </div>

              <div class="flex col-4 justify-center">
                <calc-select v-model={configStore.name} class="!h-22px">
                  {renderList(configStore.config_list, item => (
                    <calc-option value={item}>{item}</calc-option>
                  ))}
                </calc-select>
              </div>

              <div class="flex col-4 justify-center">
                <calc-select class="!h-22px">
                  <calc-option value={0}>攻击属性：自适应</calc-option>
                  <calc-option value={1}>攻击属性：火</calc-option>
                  <calc-option value={2}>攻击属性：冰</calc-option>
                  <calc-option value={3}>攻击属性：光</calc-option>
                  <calc-option value={4}>攻击属性：暗</calc-option>
                </calc-select>
              </div>

              <div class="flex col-4 justify-center">
                <calc-select class="!h-22px">
                  <calc-option value={0}>计算模式：减枝</calc-option>
                  <calc-option value={1}>计算模式：全部</calc-option>
                </calc-select>
              </div>
              <div class="flex col-4 justify-center">
                <calc-button class="w-80% !h-28px" onClick={calc}>
                  开始计算
                </calc-button>
              </div>
            </div>
          </div>
        )
      }
      return <div></div>
    }
  })
</script>
<style lang="scss">
  .main {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    background-repeat: no-repeat;
    background-size: cover;

    color: #e9c558;
    // font-size: 12px;

    .header {
      display: flex;
      align-items: flex-end;
      z-index: 2;
      height: 26px;
    }

    .footer {
      display: flex;
      align-items: center;
      justify-content: end;
      z-index: 2;
      height: 48px;
    }

    .center {
      flex: 1;
      overflow-y: auto;
      overflow-x: hidden;
      z-index: 2;
    }
  }

  .main::after {
    content: "";
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(50, 50, 50, 0.75);
  }
</style>
