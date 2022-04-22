<script lang="tsx">
  import { defineComponent, ref, watch } from "vue"
  import profile from "./overview/profile.vue"
  import equip from "./overview/equip.vue"
  import jade from "./overview/jade.vue"
  import clothes from "./overview/clothes.vue"

  export default defineComponent({
    components: { profile, equip, jade, clothes },
    setup() {
      return () => (
        <div class="detail">
          <div>
            <profile class="ml-auto mr-auto"></profile>
            <calc-collapse class="w-510px" title="装备打造">
              <equip />
            </calc-collapse>
            <calc-collapse class="w-510px" title="时装及宠物装备">
              <clothes />
            </calc-collapse>
          </div>
          <div>
            <calc-collapse class="w-510px" title="辟邪玉">
              <jade />
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
    margin: 5px;
    width: 100%;
  }
</style>
