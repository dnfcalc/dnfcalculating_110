<script lang="tsx">
  import api from "@/api"
  import { IAnyResultInfo } from "@/api/character/type"
  import Profile from "@/components/internal/profile.vue"
  import { skill_icon } from "@/pages/character/skills/sub/utils"
  import { useAppStore, useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store"
  import { toMap, to_percent } from "@/utils"
  import { computed, defineComponent, onMounted, render, renderList } from "vue"
  import { useRoute } from "vue-router"
  import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
  import { useOpenWindow } from "@/hooks/open"

  export default defineComponent({
    async setup() {
      const route = useRoute()
      const uid = (route.query.res as string) ?? ""
      const appStore = useAppStore()
      const configStore = useConfigStore()
      const basicStore = useBasicInfoStore()
      const openUrl = useOpenWindow()
      const ranks = await api.getRank(uid)
      const token = ranks.token

      configStore.$patch({ token })

      appStore.title = "排行数据(仅供参考)"

      const max = ranks.rank[0][0][0]

      onMounted(window.removeLoading)

      function equInfo(id: number) {
        return basicStore.equipment_list.filter(item => item.id == id)[0] ?? undefined
      }

      async function calc(ids: number[]) {
        ranks.setInfo.single_set = ids
        const saveData = await api.calc(
          {
            setInfo: ranks.setInfo
          },
          true
        )
        openUrl(`/result?res=${saveData.id}`, { width: 890, height: 600 })
      }

      return () => (
        <>
          <div class="flex flex-col h-full m-0 rank">
            {renderList(ranks.rank, (item, index) => (
              <div class="item">
                {renderList(item[1], equ => (
                  <EquipTips class="mr-5px" eq={equInfo(equ)} canClick={false} show-tips={false}></EquipTips>
                ))}
                <calc-button class="w-120px h-30px ml-20px" onClick={() => calc(item[1])}>
                  {(item[0][0] / 1000000 > 1 ? item[0][0] / 1000000 : item[0][0]).toFixed(0)} | {((item[0][0] / max) * 100).toFixed(2)}%
                </calc-button>
              </div>
            ))}
          </div>
        </>
      )
    }
  })
</script>

<style lang="scss" scoped>
  .rank {
    background-color: rgba(0, 0, 0, 0.75);
    overflow-y: auto;
    .item {
      text-shadow: none !important;
      height: 40px;
      line-height: 40px;
      display: flex;
      align-items: center;
      margin: 10px;

      :nth-child(3) {
        padding-left: 10px;
      }

      :nth-child(4) {
        padding-left: 10px;
      }

      :nth-child(9) {
        padding-left: 10px;
      }

      :nth-child(12) {
        padding-left: 10px;
      }
    }
  }
</style>
