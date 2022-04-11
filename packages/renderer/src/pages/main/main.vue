<script lang="tsx">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  import { defineComponent, onMounted, Suspense } from "vue"
  import { useRoute, useRouter } from "vue-router"

  export default defineComponent(() => {
    const char = useRoute().params.name as string

    return () => (
      <div
        class="main"
        style={"background-image:url(./images/characters/" + char + "/bg.jpg)"}
      >
        <div class="header">
          <calc-tabs route>
            <calc-tab value={"/equipment/" + char}>装备</calc-tab>
            <calc-tab value={"/character/" + char}>技能</calc-tab>
          </calc-tabs>
        </div>
        <div class="center">
          <Suspense>
            <router-view></router-view>
          </Suspense>
        </div>
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
