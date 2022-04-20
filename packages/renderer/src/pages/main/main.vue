<script lang="tsx">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  import { useCharacterStore } from "@/store"
  import { useAppStore } from "@/store/app"
  import { defineComponent } from "vue"
  import { useRoute } from "vue-router"

  export default defineComponent(() => {
    const char = useRoute().query.name as string
    const appStore = useAppStore()
    const characterStore = useCharacterStore()
    characterStore.newCharacter(char).then(() => {
      appStore.$patch({ title: characterStore.name })
    })

    return () => {
      if (characterStore.alter) {
        return (
          <div class="main" style={"background-image:url(./images/characters/" + characterStore.alter + "/bg.jpg)"}>
            <div class="header">
              <calc-tabs route>
                <calc-tab value="/character/equips">装备</calc-tab>
                <calc-tab value="/character/skills">技能</calc-tab>
                <calc-tab value="/character/profile">打造</calc-tab>
              </calc-tabs>
            </div>
            <div class="center">{characterStore.alter && <router-view></router-view>}</div>
            <div class="footer">
              <div class="flex col-3 justify-center">
                <calc-button>全局重置</calc-button>
              </div>
              <div class="flex col-3 justify-center">
                <calc-button>开始计算</calc-button>
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
    font-size: 12px;
    .header,
    .footer {
      height: 5%;
      max-height: 26px;
    }

    .header {
      display: flex;
      align-items: flex-end;
      z-index: 2;
    }

    .footer {
      display: flex;
      align-items: center;
      justify-content: end;
      z-index: 2;
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
