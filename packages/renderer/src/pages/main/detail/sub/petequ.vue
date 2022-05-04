<script lang="tsx">
  import { computed, defineComponent, renderList } from "vue"
  import { useCharacterStore } from "@/store"

  export default defineComponent({
    name: "petequ",
    setup(props, { emit, slots }) {
      const characterStore = useCharacterStore()
      const currentInfo = function <T>(name: string, defaultValue?: T) {
        return computed<string | number>({
          get() {
            return characterStore.getForge("petequ", name) ?? defaultValue ?? 0
          },
          set(val) {
            characterStore.setForge("petequ", name, val)
          }
        })
      }

      // 红
      const red = currentInfo("red", 0)
      // 绿
      const green = currentInfo("green", 0)
      // 蓝
      const blue = currentInfo("blue", 0)

      return () => (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="row-name">红色</div>
            <calc-select v-model={red.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">绿色</div>
            <calc-select v-model={green.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
            </calc-select>
          </div>
          <div class="equ-profile-item">
            <div class="row-name">蓝色</div>
            <calc-select v-model={blue.value} class="!h-20px flex-1">
              <calc-option value="0">无</calc-option>
            </calc-select>
          </div>
        </div>
      )
    }
  })
</script>
