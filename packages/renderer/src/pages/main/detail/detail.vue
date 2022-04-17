<script lang="tsx">
    import { defineComponent, onMounted, ref, renderList, computed } from "vue"
    import { useRoute } from "vue-router"
    import profile from "./overview/profile.vue"
    import equip from "./overview/equip.vue"
    import { IDetailInfo } from "./type"

    export default defineComponent({
        components: { profile, equip },
        setup() {
            let characterName = ref<string>("")
            const route = useRoute()
            let detail = ref<IDetailInfo[]>([
                { position: "护肩", active: true },
                { position: "上衣", active: false },
                { position: "下装", active: false },
                { position: "腰带", active: false },
                { position: "鞋", active: false },
                { position: "武器", active: false },
                { position: "称号", active: false },
                { position: "手镯", active: false },
                { position: "项链", active: false },
                { position: "辅助装备", active: false },
                { position: "戒指", active: false },
                { position: "耳环", active: false },
                { position: "魔法石", active: false },
                { position: "宠物", active: false }
            ])

            const currentDetail = computed<IDetailInfo>({
                get() {
                    return detail.value.filter(item => item.active)[0]
                },
                set(val) {}
            })

            if (typeof route.params.name === "string") characterName.value = route.params.name
            return () => (
                <div class="detail">
                    <div>
                        <profile class="ml-auto mr-auto" charName={characterName.value} detailInfo={detail.value}></profile>
                        <calc-collapse class="w-510px" title="装备打造">
                            <equip currentDetail={currentDetail.value}></equip>
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
