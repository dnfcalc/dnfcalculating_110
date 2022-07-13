<script lang="tsx">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  import { useDialog } from "@/components/hooks/dialog"
  import { useOpenWindow } from "@/hooks/open"
  import { useCharacterStore, useConfigStore } from "@/store"
  import { useAppStore } from "@/store/app"
  import { defineComponent, onMounted, ref, renderList } from "vue"
  import { useRoute } from "vue-router"

  // import Character from "@/pages/character/character/character.vue"
  // import Customize from "@/pages/character/customize/customize.vue"
  // import Equipment from "@/pages/character/equipment/equipment.vue"
  // import Detail from "@/pages/character/detail/detail.vue"
  // import Singleset from "@/pages/character/singleset/singleset.vue"

  export default defineComponent(async () => {
    const route = useRoute()
    const { confirm } = useDialog()
    const openUrl = useOpenWindow()
    const char = route.query.alter as string
    const version = route.query.version as string
    const appStore = useAppStore()
    const configStore = useConfigStore()
    const characterStore = useCharacterStore()
    const canClick = ref(true)

    onMounted(window.removeLoading)
    await characterStore.newCharacter(char, version)
    appStore.$patch({ title: characterStore.name })

    async function calc() {
      canClick.value = false
      // alert({
      //   content: () => <>暂不支持多套计算</>
      // })
      // return
      // 一堆前处理和判断，然后计算
      if (!route.path.endsWith("/singleset")) {
        let total = (configStore.equ_sort as number[][]).reduce((a, b) => a * b.length, 1)
        if (total == 0) {
          await alert({
            content: "请确保每个部位都选择了装备"
          })
          canClick.value = true
          return
        } else {
          let res = await confirm({
            content: `共计${total}组合,可能耗时较久,是否继续?`
          })
          if (res.isOk) {
            const saveData = await configStore.calc(route.path.endsWith("/singleset"))
            if (saveData) {
              if (!route.path.endsWith("/singleset")) {
                // 排行界面
                openUrl(`/ranking?res=${saveData.id}`, { width: 700, height: 650 })
              } else if (saveData) {
                // 详情界面
                openUrl(`/result?res=${saveData.id}`, { width: 890, height: 600 })
              }
            }
          }
          canClick.value = true
        }
      }
    }

    return () => {
      if (characterStore.alter) {
        return (
          <div class="main" style={"background-image:url(/images/characters/" + characterStore.alter + "/bg.jpg)"}>
            {
              // <WatermarkVue content="test" class="h-full w-full top-0 left-0 absolute" src={`/images/characters/${characterStore.alter}/bg.jpg`} />
              // <div class="header">
            }
            <div class="header">
              <calc-tabs route query={{ alter: characterStore.alter, version: characterStore.version }}>
                <calc-tab value={"/character/equips"}>装备</calc-tab>
                <calc-tab value={"/character/skills"}>技能</calc-tab>
                <calc-tab value={"/character/profile"}>打造</calc-tab>
                <calc-tab value={"/character/customize"}>自选属性</calc-tab>
                <calc-tab value={"/character/singleset"}>单套选择</calc-tab>
              </calc-tabs>
            </div>
            <div class="center">
              {characterStore.alter && (
                <router-view>
                  {
                    //   ({ Component }: { Component: any }) => {
                    //   return (
                    //     <KeepAlive>
                    //       <Component is={false} />
                    //     </KeepAlive>
                    //   )
                    // }
                  }
                </router-view>
              )}
            </div>

            <div class="footer">
              <div class="flex col-4 justify-center">
                <calc-select onChange={characterStore.calc} v-model={configStore.carry_type} class="!h-22px">
                  {renderList(characterStore.carry_type_list, (item, index) => (
                    <calc-option value={item}>{item}</calc-option>
                  ))}
                </calc-select>
              </div>

              <div class="flex col-4 justify-center" style="display:none">
                <calc-select v-model={configStore.name} class="!h-22px">
                  {renderList(configStore.config_list, item => (
                    <calc-option value={item}>{item}</calc-option>
                  ))}
                </calc-select>
              </div>

              <div class="flex col-4 justify-center">
                <calc-button class="w-80% !h-28px" disabled={!canClick.value} onClick={calc}>
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

      width: 100%;
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
