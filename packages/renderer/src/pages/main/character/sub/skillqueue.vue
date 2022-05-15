<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList } from "vue"
  import { useCharacterStore, useConfigStore } from "@/store"
  import { skill_icon } from "./utils"
  import draggable from "vuedraggable"

  export default defineComponent({
    name: "skillqueue",
    components: {
      draggable
    },
    setup(props, { emit, slots }) {
      const characterStore = useCharacterStore()
      const configStore = useConfigStore()
      const canChooseSkill = computed(() => configStore.data.skill_set.filter(item => item.level > 0 && item.damage))

      const list2 = ref([])

      const item = (item: any, index: number) => {
        return (
          <div class="w-28px h-28px m-2px">
            <img src={skill_icon(characterStore.alter, item.element.name)} />
          </div>
        )
      }

      return () => (
        <div class="w-300px">
          <div class="skill-slots subitem" style="height:120px">
            <div class="head-sec">技能队列设置</div>
            <div class="body-sec">
              <draggable class="flex w-300px flex-wrap" v-model:list={canChooseSkill.value} itemKey="name">
                {{
                  item: item
                }}
              </draggable>
            </div>
          </div>
          <div></div>
        </div>
      )
    }
  })
</script>

<style lang="scss"></style>
