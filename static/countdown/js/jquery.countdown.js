(function( $ ) {
	function tolist(num) {
		if (num > 9) {
			string = num.toString();
		} else {
			string = '0' + num.toString();
		}

		new_sting = '';
		for (var i = 0; i < string.length; i++) {
			new_sting += '<span class="b-countdown__number">' + string.charAt(i) + '</span>';
		}
		return new_sting;
	}

	$.fn.countdown = function( options ) {
		var settings = $.extend( {
			'date': new Date(2013, 12, 01, 0, 0, 0)
		}, options);

		var $this = this;

		var countdown_object = countdown(
			settings.date,
			function(ts) {
				if (ts.days || ts.hours || ts.minutes || ts.seconds) {

					$this.find('.days').html(tolist(ts.days));
					$this.find('.hours').html(tolist(ts.hours));
					$this.find('.minutes').html(tolist(ts.minutes));
					$this.find('.seconds').html(tolist(ts.seconds));

				} else {
					window.clearInterval(countdown_object);
				}
			}
		);

		return this;
	};
})(jQuery);
