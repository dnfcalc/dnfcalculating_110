<script lang="tsx">
  import { computed, defineComponent, reactive, ref, renderList } from "vue"
  import { useCharacterStore } from "@/store"
  import { skill_icon } from "./utils"
  export default defineComponent({
    name: "hotkey",
    components: {},
    setup(props, { emit, slots }) {
      const characterStore = useCharacterStore()
      // const skillList = computed(() => {
      //   return characterStore.skill_set.filter(item => item.direct)
      // })
      return () => (
        <div class="w-240px">
          <div class="skill-slots subitem mt-2%" style="height:120px">
            <div class="head-sec">技能快捷键设置</div>
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
              <div class="flex flex-row ml-2 mr-2 mt-2">
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
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .skill-slot-item {
    height: 28px;
    width: 28px;
    background-color: black;
    border: rgb(29, 29, 29) solid 1px;
    margin: 1px;
  }
</style>
