<script lang="tsx">
  import { useBasicInfoStore } from "@/store"
  import { defineComponent, onMounted, ref, renderList } from "vue"
  import { useRouter } from "vue-router"
  import openURL from "@/utils/openURL"
  import { IAlterInfo } from "@/api/info/type"

  function sub_icon(sub: number) {
    return {
      backgroundImage: `url(./images/adventure/sub/${sub}.png)`
    }
  }

  function job_icon(job: string) {
    return {
      backgroundImage: `url(./images/adventure/jobs/${job}.png)`
    }
  }

  interface IAdventureInfo {
    name: string
    alters: string[]
  }

  export default defineComponent(() => {
    const router = useRouter()
    const basicInfoStore = useBasicInfoStore()

    // 获取角色相关信息，判定是否开放
    function choose_job(child: IAlterInfo) {
      return () => {
        if (child.url) {
          openURL(child.url)
          return
        }
        if (ignores.includes(child.name)) {
          return
        }
        console.log(child)
        if (child.name === "spitfire_female") {
          openURL("/character?name=" + child.name, { width: 1280, height: 900 }, router)
        } else {
          openURL("/show", { width: 800, height: 800 }, router)
        }
      }
      // router.push("/character/" + alter)
    }

    const ignores = ["sponsor", "empty"]

    // function getName(name: string) {
    //   return ignores.includes(name) ? "" : name
    // }

    return () => (
      <div class="bg-cover bg-no-repeat pt-8 pb-12 pl-4 home">
        {renderList(basicInfoStore.adventure_info, (job, index) => (
          <div class="flex flex-row">
            <div class="bg-no-repeat bg-center flex flex-wrap h-25 w-30 job-icon-box justify-center items-center relative">
              <div class="bg-center bg-no-repeat h-22.5 w-30" style={sub_icon(index)}></div>
            </div>
            {renderList(job.children, (child, j) => (
              <div onClick={choose_job(child)} class="cursor-pointer h-22.5 m-1 w-30 duration-300 job-box box-border relative">
                <div class="bg-no-repeat h-full w-full z-2 duration-200 job-border absolute hover:bg-hex-ffd7002e"></div>
                <div class="text-xs text-center w-full bottom-1 text-hex-bea347 absolute">{child.title}</div>
                <div class="bg-no-repeat bg-auto bg-clip-content h-full w-full z-1 overflow-hidden" style={job_icon(child.name)}></div>
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
    background-image: url(./images/adventure/bg.jpg);
    background-size: 100% 100%;

    .job-icon-box {
      background-image: url(./images/adventure/flash.png);
    }

    .job-box {
      .job-border {
        background-image: url(./images/adventure/border.png);
      }
    }
  }
</style>
