<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"
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
      let canChooseSkill = ref(configStore.data.skill_que)

      watch(configStore.data.skill_set, val => {
        let tem: { name: string; id: number }[] = []
        // 重新排序一下
        //   let temp =
        //     configStore.data.skill_que?.map((item, index) => {
        //       item.id = index
        //       return item
        //     }) || []
        //   let toRemove = []
        //   let toAdd = []
        //   // 根据次数删除
        //   temp.map(item => item.name)
        // })
        // todo 根据次数修改自动添加/删除技能
        configStore.data.skill_set.forEach(item => {
          if (item.count > 0 && item.level > 0 && item.damage) for (var i = 0; i < item.count; i++) tem.push({ name: item.name, id: 0 })
        })
        canChooseSkill.value = tem.map((item, index) => {
          item.id = index
          return item
        })
      })

      watch(canChooseSkill.value, val => {
        configStore.data.skill_que = val
      })

      const item = (item: any, index: number) => {
        return (
          <div class="h-28px m-2px w-28px">
            <img src={skill_icon(characterStore.alter, item.element.name)} />
          </div>
          // <div class="list-group-item">{item.element.name}</div>
        )
      }

      return () => (
        <div class="w-300px">
          <div class="h-100% skill-slots subitem">
            <div class="head-sec">技能队列设置</div>
            <draggable class="flex flex-wrap body-sec" v-model:list={canChooseSkill.value} group={{ name: "people", pull: "clone", put: false }} itemKey="id">
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
