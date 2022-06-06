<script lang="tsx">
  import { useBasicInfoStore } from "@/store"
  import { defineComponent, onMounted, renderList } from "vue"
  import openURL from "@/utils/openURL"
  import { IAlterInfo } from "@/api/info/type"
  import { useDialog } from "@/components/hooks/dialog"
  import api from "@/api"

  function sub_icon(sub: number) {
    return {
      backgroundImage: `url(./images/adventure/sub/${sub}.png)`
    }
  }

  function job_icon(child: IAlterInfo) {
    return {
      filter: !child.open ? `grayscale(100%)` : ``,
      backgroundImage: `url(./images/adventure/jobs/${child.name}.png)`
    }
  }

  export default defineComponent(() => {
    const basicInfoStore = useBasicInfoStore()

    const { alert, confirm, show } = useDialog()

    // 获取角色相关信息，判定是否开放
    function choose_job(child: IAlterInfo) {
      return async () => {
        if (child.url) {
          const result = await confirm({
            content: <div>是否从新页面打开?</div>
          })
          if (result.status == "ok") {
            openURL(child.url)
          }
          return
        }
        if (ignores.includes(child.name)) {
          return
        }
        if (child.open) {
          openURL("/character?name=" + child.name, { width: 1100, height: 750 })
        } else {
          await alert({
            content: "未开放的角色!"
          })
        }
      }
      // router.push("/character/" + alter)
    }

    const ignores = ["sponsor", "empty"]

    // function getName(name: string) {
    //   return ignores.includes(name) ? "" : name
    // }

    onMounted(async () => {
      if (window.ipcRenderer && process.env.NODE_ENV !== "development") {
        try {
          await api.checkUpdate(APP_VERSION)
          const res = await show({
            content: (
              <div class="text-left w-full justify-center">
                检测到更新，是否自动更新？
                <br />
                自动更新后台静默下载，下次启动时生效。
              </div>
            ),
            rejectButton: "手动更新",
            okButton: "自动更新",
            cancelButton: "取消"
          })

          if (res.status == "reject") {
            openURL("https://wwn.lanzout.com/s/dcalc")
          } else if (res.status == "ok") {
            await api.autoUpdate()
          }
        } catch {
          await alert({
            content: "自动检查更新错误,请手动检查更新"
          })
        }
      }
    })

    return () => (
      <div class="bg-cover bg-no-repeat pt-8 pb-12 pl-4 home" style="background-image: url('./images/adventure/bg.jpg')">
        {renderList(basicInfoStore.adventure_info, (job, index) => (
          <div class="flex flex-row">
            <div class="bg-no-repeat bg-center flex flex-wrap h-25 w-30 job-icon-box justify-center items-center relative" style="background-image: url('./images/adventure/flash.png')">
              <div class="bg-center bg-no-repeat h-22.5 w-30" style={sub_icon(index)}></div>
            </div>
            {renderList(job.children, (child, j) => (
              <div onClick={choose_job(child)} class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative">
                {child.open && <div class="bg-no-repeat h-full w-full z-2 duration-200 job-border absolute hover:bg-hex-ffd7002e" style="background-image: url('./images/adventure/border.png')"></div>}
                <div class="text-xs text-center w-full bottom-1 text-hex-bea347 absolute">{child.title}</div>
                <div class="bg-no-repeat bg-auto bg-clip-content h-full w-full z-1 overflow-hidden" style={job_icon(child)}></div>
              </div>
            ))}
          </div>
        ))}
      </div>
    )
  })
</script>

<style lang="scss">
  .home {
    // background-image: url($path + "bg.jpg");
    background-size: 100% 100%;

    // .job-icon-box {
    //   // background-image: url($path + "flash.png");
    // }

    // .job-box {
    //   .job-border {
    //     // background-image: url($path + "border.png");
    //   }
    // }
  }
</style>
