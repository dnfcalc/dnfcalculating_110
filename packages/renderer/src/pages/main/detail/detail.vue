<script lang="tsx">
  import { defineComponent, onMounted, ref, renderList, computed, watch } from "vue"
  import { useRoute } from "vue-router"
  import profile from "./overview/profile.vue"
  import equip from "./overview/equip.vue"

  import { useVModel } from "@vueuse/core"
  import { IDetailInfo } from "./type"

  export default defineComponent({
    components: { profile, equip },
    setup() {
      let characterName = ref<string>("")
      const route = useRoute()
      const activeIndex = ref(0)

      let detail = ref<IDetailInfo[]>([
        { position: "头肩", fumo: 0 },
        { position: "上衣", fumo: 0 },
        { position: "下装", fumo: 0 },
        { position: "腰带", fumo: 0 },
        { position: "鞋", fumo: 0 },
        { position: "武器", fumo: 0 },
        { position: "称号", fumo: 0 },
        { position: "手镯", fumo: 0 },
        { position: "项链", fumo: 0 },
        { position: "辅助装备", fumo: 0 },
        { position: "戒指", fumo: 0 },
        { position: "耳环", fumo: 0 },
        { position: "魔法石", fumo: 0 },
        { position: "宠物", fumo: 0 }
      ])
      watch(
        detail,
        () => {
          console.log(detail.value[activeIndex.value].fumo)
        },
        {
          deep: true
        }
      )

      if (typeof route.params.name === "string") characterName.value = route.params.name
      return () => (
        <div class="detail">
          <div>
            <profile class="ml-auto mr-auto" charName={characterName.value} detailInfo={detail.value} v-model:activeIndex={activeIndex.value}></profile>
            <calc-collapse class="w-510px" title="装备打造">
              <equip v-model:currentDetail={detail.value[activeIndex.value]}></equip>
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
    height: 100%;
    width: 100%;
  }
</style>
