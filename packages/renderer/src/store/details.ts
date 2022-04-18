import { defineStore } from "pinia"

export const useDetailsStore = defineStore("details", {
  state() {
    return {
      part: "头肩",
      display_parts: ["头肩", "上衣", "下装", "腰带", "鞋", "武器", "称号", "手镯", "项链", "辅助装备", "戒指", "耳环", "魔法石", "宠物"]
    }
  },

  actions: {
    setPart(part: string) {
      this.part = part
    }
  }
})
