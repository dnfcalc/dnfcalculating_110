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
          <div>
            <img src={skill_icon(characterStore.alter, item.element.name)} />
          </div>
        )
      }

      return () => (
        <div class="w-300px">
          <div class="skill-slots subitem" style="height:120px">
            <div class="head-sec">技能队列设置</div>
            <div class="body-sec">
              <div class="flex flex-row ml-2 mr-2">
                <div class="skill-slot-item">
                  <img src={`./images/characters/${characterStore.alter}/skill/交叉射击.png`} />
                </div>
                <div class="skill-slot-item"></div>
                <div class="skill-slot-item"></div>
                <div class="skill-slot-item"></div>
                <div class="skill-slot-item"></div>
                <div class="skill-slot-item"></div>
                <div class="skill-slot-item"></div>
              </div>
            </div>
          </div>
          <div>
            <draggable class="list-group" v-model:list={canChooseSkill.value} group={{ name: "people", pull: "clone", put: false }} itemKey="name">
              {{
                item: item
              }}
            </draggable>
          </div>
          -------------------------------------------------
          <div>
            <draggable class="list-group" v-model:list={list2.value} group="people" itemKey="name">
              {{
                item: item
              }}
            </draggable>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss"></style>
