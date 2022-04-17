<script lang="tsx">
    import { defineComponent, onMounted, ref, renderList } from "vue"
    import { useRoute } from "vue-router"
    import profile from "./overview/profile.vue"
    import { IDetailInfo } from "./type"

    export default defineComponent({
        components: { profile },
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

            if (typeof route.params.name === "string") characterName.value = route.params.name
            return () => (
                <div class="detail">
                    <div>
                        <profile charName={characterName.value} detailInfo={detail.value}></profile>
                        <calc-collapse title="装备打造">
                            <div>测试一下</div>
                        </calc-collapse>
                    </div>

                    <div>
                        <div class="item">
                            <div class="name">耳环</div>
                            <div class="d-choose">
                                <div class="w-30% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                                <div class="w-30% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                                <div class="w-30% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                                <div class="w-20% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                                <div class="w-20% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                                <div class="w-20% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                                <div class="w-20% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                                <div class="w-100% d-choose-item">
                                    <calc-select></calc-select>
                                </div>
                            </div>
                        </div>
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

        .item {
            display: flex;
            align-items: center;
            margin: 5px;

            .i-select {
                height: 20px !important;
                width: 100% !important;
            }
            .name {
                color: #e9c556;
                font-size: 12px;
                width: 50px;
            }

            .d-choose {
                display: flex;
                flex-wrap: wrap;
                width: 100%;
                justify-content: space-between;

                .d-choose-item {
                    height: 27px;
                    display: flex;
                    align-items: center;
                }
            }
        }
    }
</style>
