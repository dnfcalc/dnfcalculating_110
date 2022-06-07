<script lang="tsx">
  // This starter template is using Vue 3 <script setup> SFCs
  // Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
  import { computed, defineComponent, onUnmounted, Suspense } from "vue"
  import { useRoute } from "vue-router"
  import { useAppStore } from "@/store/app"
  import api from "@/api"
  import { useDialog } from "@/components/hooks/dialog"

  export default defineComponent({
    setup() {
      const appStore = useAppStore()

      const { alert, render } = useDialog()

      const title = computed(() => {
        const route = useRoute()
        return route.meta.title ?? appStore.title
      })

      if (process.env.NODE_ENV !== "development") {
        const timer = setInterval(async () => {
          try {
            await api.heartbeat()
          } catch (e) {
            clearInterval(timer)
            await alert({
              content: "网络连接中断"
            })
          }
        }, 5000)

        onUnmounted(() => {
          clearInterval(timer)
        })
      }

      return () => (
        <>
          <div
            class="bg-hex bg-gradient-to-t flex from-hex-273e69 to-hex-335793 h-6 px-2 top-0 right-0 left-0 leading-6  z-999 app-header layout-title items-center justify-between fixed"
            style="-webkit-app-region: drag"
          >
            <div class="h-4 leading-4 w-4" style="background-image:url('./favicon.ico');background-size: 100% 100%;"></div>
            <div class="text-xs text-shadow header">
              {title.value} {`(${APP_VERSION})`}
            </div>
            <div class="flex items-center">
              <div onClick={appStore.minimize} class="cursor-pointer min-icon h-4  text-center mr-4 text-hex-f0d070 text-opacity-72 w-4 hover:text-opacity-100"></div>
              <div onClick={appStore.close} class="cursor-pointer h-4 text-center  text-hex-f0d070 text-opacity-72  w-4 close-icon hover:text-opacity-100"></div>
            </div>
          </div>
          <div class="w-full pt-6 overflow-y-auto" style="height:calc(100% - 24px);">
            <Suspense>
              <router-view></router-view>
            </Suspense>
          </div>
          {render()}
        </>
      )
    }
  })
</script>

<style scoped>
  .app {
    height: 100%;
  }
</style>
