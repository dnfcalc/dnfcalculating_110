<script lang="tsx">
  import api from "@/api"
  import { IRecommendInfo, IRecommendRequest } from "@/api/info/type"
  import { isShow, onShow } from "@/components/hooks/show"
  import EqIconVue from "@/components/internal/equip/eq-icon.vue"
  import { useCharacterStore, useConfigStore } from "@/store"
  import { useAsyncState } from "@vueuse/core"
  import { computed, defineComponent, reactive, renderList } from "vue"
  export default defineComponent({
    setup() {
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()

      const params = reactive<IRecommendRequest>({
        page: 1,
        size: 7,
        keyword: "",
        alter: characterStore.alter
      })

      const { state, execute } = useAsyncState(
        () => {
          return api.recommends(params)
        },
        {
          data: [],
          pageIndex: 0,
          pageSize: 7,
          totalCount: 1
        },
        {
          resetOnExecute: false,
          immediate: false
        }
      )

      const visible = isShow()

      onShow(execute, { immediate: true })

      const totalPage = computed(() => Math.ceil(state.value.totalCount / params.size))

      function apply(item: IRecommendInfo) {
        return () => {
          configStore.importSingle(item.equips.map(r => r.id))
          item.equips.forEach(eq => {
            eq.props = eq.props ?? []
            if (eq.props.length > 0) configStore.customize[eq.id ?? 0] = eq.props as number[]
          })
          visible.value = false
        }
      }

      return () => {
        return (
          <div class="h-132 py-2 px-4 text-hex-e9c556 w-120 overflow-y-auto">
            <div class="flex space-x-4 w-full box-border items-center">
              <calc-autocomplete class="flex-1" placeholder="输入关键字搜索流派搭配" v-model={params.keyword}></calc-autocomplete>
              <calc-button onClick={execute}>搜索</calc-button>
            </div>
            <div class="h-108">
              {renderList(state.value.data, item => {
                return (
                  <div class="mx-auto  my-2 ">
                    <div class="flex h-6 text-sm leading-6 w-96 items-center justify-between">
                      <span>{item.name}</span>
                      <span>[{item.author}]</span>
                    </div>
                    <div class="flex items-center justify-between">
                      <div class="flex items-center">
                        {renderList(item.equips.slice(0, 12), eq => {
                          return <EqIconVue class="px-1px" eid={eq.id}></EqIconVue>
                        })}
                      </div>
                      <calc-button onClick={apply(item)}>应用</calc-button>
                    </div>
                  </div>
                )
              })}
            </div>
            <calc-pagination disabled={!visible.value} class="h-8" v-model:page={params.page} onChange={() => execute()} totalPage={totalPage.value}></calc-pagination>
            <a href="https://www.skycity.top/dictionary?from=dcalc" target="__blank" class="flex w-full text-hex-f4e713 justify-center">
              Power by SkyCity
            </a>
          </div>
        )
      }
    }
  })
</script>
