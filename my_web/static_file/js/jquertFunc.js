function clearDefault(a){a.defaultValue==a.value&&(a.value="")}function resetDefault(a){isEmpty(a.value)&&(a.value=a.defaultValue)}function isEmpty(a){return null==a||"undefined"==a||0==a.length?!0:!/\S/.test(a)}jQuery(document).ready(function(){jQuery(".ui-tabs-nav > li > a").mouseover(function(a){if(a.target==this){var b=jQuery(this).parent().parent().children("li"),c=jQuery(this).parent().parent().parent().children(".ui-tabs-panel"),d=jQuery.inArray(this,jQuery(this).parent().parent().find("a"));c.eq(d)[0]&&(b.removeClass("ui-tabs-selected").eq(d).addClass("ui-tabs-selected"),c.addClass("ui-tabs-hide").eq(d).removeClass("ui-tabs-hide"))}}),jQuery("#proNav").hover(function(){jQuery("#trigger1").addClass("mu_cur")},function(){jQuery("#trigger1").removeClass("mu_cur"),jQuery(this).hide()}),jQuery("#trigger1").mouseover(function(){jQuery(this).addClass("mu_cur"),jQuery("#proNav").show()}),jQuery(".nav .a1").mouseover(function(){jQuery("#trigger1").removeClass("mu_cur"),jQuery("#proNav").hide()})});