<script lang="tsx">
  import { useCharacterStore } from "@/store"
  import { defineComponent } from "vue"
  import Cp from "./sub/cp.vue"
  import Hotkey from "./sub/hotkey.vue"
  import Skill from "./sub/skill.vue"
  import Skillqueue from "./sub/skillqueue.vue"

  export default defineComponent({
    setup() {
      const characterStore = useCharacterStore()
      return () => (
        <div class="flex character">
          <div class="flex p-5px">
            <Skill></Skill>
          </div>
          <div class="w-240px">
            <div class="h-220px mt-2% subitem">
              <Cp></Cp>
            </div>
            <div class="mt-2% skill-slots subitem">{characterStore.is_delear && <Hotkey></Hotkey>}</div>
          </div>
          {characterStore.is_delear && (
            <div class="flex p-5px pl-35px">
              <Skillqueue></Skillqueue>
            </div>
          )}
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
