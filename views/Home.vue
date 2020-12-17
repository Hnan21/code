<template>
  <div>
    <Header></Header>
    <Banner></Banner>
    <Footer></Footer>

  </div>
</template>

<script>
import Footer from "@/components/Footer";
import Banner from "@/views/Banner";
import Header from "@/components/Header";

export default {
  name: "Home",
  components:{
    Header: Header,
    Footer: Footer,
    Banner: Banner,
  },
}
</script>

<style scoped>

</style>