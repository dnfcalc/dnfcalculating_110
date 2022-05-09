<script lang="tsx">
  import { defineComponent, ref, watch } from "vue"
  import profile from "./sub/profile.vue"
  import equip from "./sub/equip.vue"
  import jade from "./sub/jade.vue"
  import clothes from "./sub/clothes.vue"
  import others from "./sub/others.vue"
  import petequ from "./sub/petequ.vue"

  export default defineComponent({
    components: { profile, equip, jade, clothes, others, petequ },
    setup() {
      return () => (
        <div class="detail">
          <div>
            <profile class="ml-auto mr-auto"></profile>
            <calc-collapse class="w-510px" title="装备打造">
              <equip />
            </calc-collapse>
            <calc-collapse class="w-510px" title="装扮部分">
              <clothes />
            </calc-collapse>
          </div>
          <div>
            <calc-collapse class="w-510px" title="宠物装备">
              <petequ />
            </calc-collapse>
            <calc-collapse class="w-510px" title="辟邪玉">
              <jade />
            </calc-collapse>

            <calc-collapse class="w-510px" title="其它">
              <others />
            </calc-collapse>
          </div>
        </div>
      )
    }
  })
</script>

<style lang="scss">
  .detail {
    display: flex;
    width: 100%;
    justify-content: space-around;
  }

  .equ-profile {
    width: 100%;

    .equ-profile-item {
      width: 100%;
      height: 20px;
      display: flex;
      margin-top: 5px;
      margin-bottom: 5px;
      align-items: center;

      .row-name {
        flex: 0 0 50px;
        text-align: center;
      }

      :not(:last-child) {
        margin-right: 10px !important;
      }

      .i-select-label {
        margin-right: 0px !important;
      }
    }
  }
</style>
