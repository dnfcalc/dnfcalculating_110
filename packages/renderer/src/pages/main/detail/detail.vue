<script lang="tsx">
  import { defineComponent, ref, watch } from "vue"
  import profile from "./overview/profile.vue"
  import equip from "./overview/equip.vue"

  import { IDetailInfo } from "./type"

  export default defineComponent({
    components: { profile, equip },
    setup() {
      return () => (
        <div class="detail">
          <div>
            <profile class="ml-auto mr-auto"></profile>
            <calc-collapse class="w-510px" title="装备打造">
              <equip></equip>
            </calc-collapse>
            <calc-collapse class="w-510px" title="时装及宠物装备"></calc-collapse>
          </div>
          <div>
            <calc-collapse class="w-510px" title="辟邪玉"></calc-collapse>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .detail {
    display: flex;
    margin: 5px;
    width: 100%;
  }
</style>
