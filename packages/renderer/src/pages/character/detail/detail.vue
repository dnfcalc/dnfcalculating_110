<script lang="tsx">
  import Profile from "@/components/internal/profile.vue"
  import { defineComponent, ref } from "vue"
  import Clothes from "./sub/clothes.vue"
  import Equip from "./sub/equip.vue"
  import Jade from "./sub/jade.vue"
  import Others from "./sub/others.vue"
  import Petequ from "./sub/petequ.vue"
  import Special from "./sub/special.vue"

  export default defineComponent({
    components: { Profile, Equip, Jade, Clothes, Others, Petequ, Special },
    setup() {
      const part = ref("头肩")

      return () => (
        <div class="detail">
          <div>
            <div class="bg-hex-00000078 w-510px">
              <Profile v-model:part={part.value} canChoose={true} showDetail={false} class="mr-auto ml-auto"></Profile>
            </div>
            <calc-collapse class="w-510px" title="装备打造(点击人物部位切换)">
              <Equip part={part.value} />
            </calc-collapse>
            <calc-collapse class="w-510px" title="装扮部分">
              <Clothes />
            </calc-collapse>
          </div>
          <div class="pl-20px">
            <calc-collapse class="w-510px" title="宠物装备">
              <Petequ />
            </calc-collapse>
            <calc-collapse class="w-510px" title="辟邪玉">
              <Jade />
            </calc-collapse>

            <calc-collapse class="w-510px" title="其它">
              <Others />
            </calc-collapse>
            <calc-collapse class="w-510px" title="职业特殊">
              <Special />
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
    margin-left: 25px;
    margin-right: 25px;
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
