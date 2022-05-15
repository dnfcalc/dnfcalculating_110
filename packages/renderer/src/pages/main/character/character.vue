<script lang="tsx">
  import { computed, defineComponent, onMounted, reactive, ref, renderList } from "vue"
  import { useCharacterStore } from "@/store"
  import cp from "./sub/cp.vue"
  import hotkey from "./sub/hotkey.vue"
  import skill from "./sub/skill.vue"
  import skillqueue from "./sub/skillqueue.vue"

  export default defineComponent({
    components: { cp, hotkey, skill, skillqueue },
    setup() {
      return () => (
        <div class="character flex">
          <div class="flex p-5px">
            <skill></skill>
          </div>
          <div>
            <div class="h-220px subitem mt-2%">
              <cp></cp>
            </div>
            <div class="skill-slots subitem mt-2%">
              <hotkey></hotkey>
            </div>
          </div>
          <div class="flex p-5px pl-35px">
            <skillqueue></skillqueue>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .cp {
    background-image: url(./images/common/talisman.png);
    height: 52px;
    width: 168px;
    margin: 0 auto;
    margin-top: 5px;
    display: flex;
    .talisman {
      width: 28px;
      margin-left: 9px;
      margin-top: 11px;
    }
    .rune {
      width: 28px;
      margin-left: 5px;
      margin-top: 12px;
    }
    .rune:nth-child(2) {
      margin-left: 21px;
    }
  }
  .skill-slot-item {
    height: 28px;
    width: 28px;
    background-color: black;
    border: rgb(29, 29, 29) solid 1px;
    margin: 1px;
  }
</style>
